from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import os

browser = webdriver.Firefox()


browser.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
username="hominhhuy3239@gmail.com"
password="DGoceaiwk29524"
browser.find_element_by_xpath('//input[@type="email"]').send_keys(username)
browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(2)
browser.find_element_by_xpath('//input[@type="password"]').send_keys(password)
browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(2)


browser.get("https://www.youtube.com")
browser.find_element_by_xpath("//ytd-button-renderer[@class='style-scope ytd-masthead style-suggestive size-small']").click()
time.sleep(2)


browser.get("https://www.youtube.com/watch?v=m2mR0osyqFI")
time.sleep(2)
browser.execute_script("window.scrollTo(0, 400);")
comment="Good"
box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "placeholder-area")))
box.click()
os.system("echo %s| clip" % comment)
keyboard.send("ctrl+v")

submit = browser.find_element_by_id("submit-button")
submit.click()
time.sleep(2)

browser.quit()