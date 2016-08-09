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

import pymysql
pymysql.install_as_MySQLdb()
from company.redshift_connection import *


def session():
	profile = webdriver.FirefoxProfile()
	profile.set_preference('browser.download.folderList', 2)
	profile.set_preference('browser.download.manager.showWhenStarting', False)
	profile.set_preference('browser.download.dir', 'path')
	profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/xml,text/plain,text/xml,image/jpeg,text/csv'))
	return profile

def login(browser):
	time.sleep(2)
	browser.get('https://www.myurl.com/login')
	assert 'My URL' in browser.title
	time.sleep(2)
	elem = browser.find_element_by_id('login')  # find the User Id textbox
	elem.clear()
	elem.send_keys('') # your username
	elem = browser.find_element_by_id('password')  # find the Password textbox
	elem.clear()
	elem.send_keys('') # your password
	elem.send_keys(Keys.RETURN)

def urlCreation():

	date_start = '01/01/2015'
	date_end = time.strftime('%m/%d/%Y')
	url = 'https://www.myurl.com/user/7hbx2rmd855kk375/user_reports/run?utf8=%E2%9C%93&report_criteria%5Buser_account_tokens%5D%5B%5D=ALL&commit=Run+User+Report'
	url = url + '&report_criteria%5Bstart_date%5D=' + date_start
	url = url + '&report_criteria%5Bend_date%5D=' + date_end
	return url


def downloadReport(browser, url):
	browser.get(url)
	time.sleep(2)
	elem = browser.find_element_by_id('download_form')
	elem.click()
	wait = WebDriverWait(browser, 60)
	proceed = wait.until(EC.text_to_be_present_in_element((By.XPATH,'//div[@id="categorized-downloads"]/div/div[1]/span[2]/a'),'Download'))
	elem = browser.find_element_by_xpath('//div[@id="categorized-downloads"]/div/div[1]/span[2]/a')
	href = elem.get_attribute('href')
	browser.get(href)

def importIntoRedshift():
	inputFileName = '/Users/ValP/Documents/Personnal/Scrapper/scrap_folder/user_01_01_2015_' + time.strftime('%m_%d_%Y') + '.csv'
	r = RedshiftConnection()
	r.load_csv(inputFileName, 'user_report','analytics', if_exists='replace', escape_first_n_lines=1)
	r.close()

if __name__ == "__main__":
	

	browser = webdriver.Firefox(session())
	time.sleep(5)
	login(browser)
	url = urlCreation()
	time.sleep(3)
	downloadReport(browser, url)
	time.sleep(4)
	browser.close()
	importIntoRedshift()

	# print urlCreation()
		# to combine the resulting files see the python notebook [combining_data_scrapper.ipynb]






