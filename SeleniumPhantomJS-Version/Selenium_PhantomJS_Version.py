import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_info(url):
#########################################################
##### Request Header for Phantomjs
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
    
    ##注意修改executable_path为自己PhantomJS安装目录的绝对路径
    driver = webdriver.PhantomJS(executable_path='D:/Python/phantomjs.exe', desired_capabilities=dcap)  

####################################################################################
##### JavaScrirt contens of website
    titleList = []
    driver.get(url)
    driver.implicitly_wait(20)
    author = driver.find_element_by_xpath('//span[@class="name"]/a').text
    data  = driver.find_element_by_xpath('//span[@class="publish-time"]').text
    word  = driver.find_element_by_xpath('//span[@class="wordage"]').text
    view  = driver.find_element_by_xpath('//span[@class="views-count"]').text
    comment  = driver.find_element_by_xpath('//span[@class="comments-count"]').text
    like  = driver.find_element_by_xpath('//span[@class="likes-count"]').text
####################################################################################

####################################################################################
##### Click to autoload contents of website
    loadmore = driver.find_element_by_xpath('//div[@class="include-collection"]/a[@class="show-more"]')
    actions = ActionChains(driver)
    actions.move_to_element(loadmore)
    actions.click(loadmore)
    actions.perform()
    time.sleep(2)   
    includedList  = driver.find_elements_by_xpath('//div[@class="include-collection"]/a/div')
####################################################################################

###################################################################################
######### Iterate Tag A's text contents to List titleList
    for i in includedList:
        titleList.append(i.text)
###################################################################################

##################################################################################
### The last to print all of information gotten by program. 
    print(author, data, word, view, comment, like, titleList)
#################################################################################

#################################################################################
### Calling program and transmitting Arguments
def main():
    url = 'http://www.jianshu.com/p/c9bae3e9e252'
    get_info(url)
##################################################################################

###########################################
#### Run the program
if __name__ == '__main__':
    main()
##########################################
## Done
