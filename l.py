# python2
from selenium import webdriver
import time

#importing important files
import requests, json
from bs4 import BeautifulSoup
import unicodecsv as csv

# activate the selenium module for headless browser
# so that the google chrome can run in background
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options = options)


START_URL = "http://www.priceofweed.com/prices/United-States/Georgia.html"

#Function defined to scrape URL of different NGOs from the website
print "scraping links....."
def scrape_ngo_list(page_url):
	SMRtable = driver.find_element_by_xpath('//*[@id="contentdt"]/table[2]/tbody')
	for i in SMRtable.find_element_by_xpath('.//tr'):
		# for n in i.find_element_by_xpath('.//td'):
			print i.get_attribute('innerHTML')
scrape_ngo_list(START_URL)


