from selenium import webdriver
from os.path import join, dirname, abspath
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from random import randint
import time

driver = webdriver.Chrome()
driver.get("https://my.sa.ucsb.edu/gold/login.aspx")
driver.execute_script("document.getElementById('pageContent_userNameText').value = 'victorcheng';")
driver.execute_script("document.getElementById('pageContent_passwordText').value = '';")
driver.execute_script("document.getElementById('pageContent_loginButton').click();")

