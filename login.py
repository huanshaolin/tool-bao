from selenium import webdriver
import time
from fake_useragent import UserAgent


ua = UserAgent()
user_agent = ua.random
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(executable_path="D:\\Software\\chromedriver.exe",chrome_options=options)
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

browser.get("https://accounts.google.com/ServiceLogin/identifier?service=youtube&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

usernameEle = browser.find_element_by_id("identifierId") 
usernameEle.send_keys("hominhhuy3239@gmail.com")   
nextEle = browser.find_element_by_id("identifierNext")
# browser.profile.set_preference("javascript.enabled", False)
nextEle.click()
# print(browser.page_source)


time.sleep(10)

browser.quit()