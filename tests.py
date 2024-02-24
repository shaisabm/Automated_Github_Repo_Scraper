import urllib.request

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.firefox.service import service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import *
from selenium.webdriver.common.by import By
import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
import re

#browser = webdriver.Firefox('/Users/shai/Downloads/geckodriver')
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())



browser.get('https://github.com/jedisct1/libsodium/blob/master/src/libsodium/Makefile.am')
files = browser.find_elements(By.CLASS_NAME,"Link--primary")

# print(files)
for element in files:
    print(element.get_attribute('href'))
browser.quit()

# web = urlopen("https://github.com/jedisct1/libsodium/tree/master/src")
# soup = BeautifulSoup(web,"html.parser")
# #print(soup.find_all(class_='react-directory-row undefined'))
# x  = soup.getText
# print(x)




