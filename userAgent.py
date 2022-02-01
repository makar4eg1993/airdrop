from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

class UserAgent():
    def openBrowser(self):
        global driver
        chrome_options = Options()
        # chrome_options.add_extension('/waextensions/metamask.crx')
        driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)

        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w')
        driver.maximize_window()
        time.sleep(10)
    def CheckUserAgent(self):
        driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")


test=UserAgent()
test.openBrowser()
test.CheckUserAgent()