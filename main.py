from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import os

profile = webdriver.FirefoxProfile("C:\\Users\\HoangHao\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\0f5za60y.default-release")
browser = webdriver.Firefox(firefox_profile=profile)

browser.get("https://www.youtube.com/watch?v=m2mR0osyqFI")

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