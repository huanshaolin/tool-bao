from selenium import webdriver
import time

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0'
PHANTOMJS_ARG = {'phantomjs.page.settings.userAgent': UA}

browser = webdriver.Firefox()

browser.get("https://accounts.google.com/ServiceLogin/identifier?service=youtube&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

usernameEle = browser.find_element_by_id("identifierId") 
usernameEle.send_keys("hominhhuy3239@gmail.com")   
nextEle = browser.find_element_by_id("identifierNext")
nextEle.click()
# print(browser.page_source)


time.sleep(20)

browser.quit()