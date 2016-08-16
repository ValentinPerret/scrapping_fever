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
import random


def login(browser, loginFile='id.txt'):
	
	browser.get('https://www.instagram.com/')
	assert 'Instagram' in browser.title

	time.sleep(2) #make it random
	elem = browser.find_elements_by_class_name('_fcn8k')  
	elem[0].click()

	logInfos = getLines(loginFile)

	elem = browser.find_element_by_name('username')
	elem.clear()
	elem.send_keys(logInfos[0].strip())

	elem = browser.find_element_by_name('password')
	elem.clear()
	elem.send_keys(logInfos[1].strip())
	elem.send_keys(Keys.RETURN)

def getLines(fileName):
	f = open(fileName)
	elements = f.readlines()
	f.close()
	return elements

def goToProfiles(browser, profileName):
	base_url = 'https://www.instagram.com/'
	profile_url = base_url + profileName
	browser.get(profile_url)

def findLastPicture(browser, className = '_nljxa'):
	elem = browser.find_element_by_xpath('//div[@class="{}"]/div[1]/a[1]'.format(className))
	href = elem.get_attribute('href')
	browser.get(href)

def commenting(browser, message = 'Lb'):
	elem = browser.find_element_by_tag_name('input')
	elem.send_keys(message)
	elem.send_keys(Keys.RETURN)

def wait():
	time.sleep(random.uniform(2,4))


if __name__ == "__main__":
	browser = webdriver.Firefox()
	login(browser)
	wait()
	for profile in getLines('profilelist.txt'):
		goToProfiles(browser, profile)
		wait()
		findLastPicture(browser)
		wait()
		commenting(browser)
	browser.close()

	# profileList = getLines('profilelist.txt')
	# for i in range(0, len(profileList)):
