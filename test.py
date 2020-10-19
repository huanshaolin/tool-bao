from selenium import webdriver
import time
class Google:

    def __init__(self,username,password):
        self.driver=webdriver.Chrome(executable_path="D:\\Software\\chromedriver.exe")
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        time.sleep(2)
        self.driver.get('https://youtube.com')
        time.sleep(5)

mylike= Google("hominhhuy3239@gmail.com","DGoceaiwk29524")