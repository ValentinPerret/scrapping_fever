from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from furl import furl
from datetime import date
import time
import datetime
import sys


browser = webdriver.Firefox()
time.sleep(2)

browser.get('https://www.thewebsite.com/') #change thewebsite by the good address
assert 'thewebsite' in browser.title
time.sleep(2)
elem = browser.find_elements_by_class_name('_fcn8k')  
elem[0].click()
elem = browser.find_element_by_name('username')
elem.clear()
elem.send_keys('Username') #user name
elem = browser.find_element_by_name('password')
elem.clear()
elem.send_keys('Password') #password
elem.send_keys(Keys.RETURN)

time.sleep(2)

browser.get('https://www.thewebsite.com/kyliejenner/') #change thewebsite by the good address

time.sleep(2)
elem = browser.find_element_by_xpath('//div[@class="_nljxa"]/div[1]/a[1]')
href = elem.get_attribute('href')
browser.get(href)

time.sleep(2)
elem = browser.find_element_by_tag_name('input')
elem.send_keys('Lb')
elem.send_keys(Keys.RETURN)

browser.close()