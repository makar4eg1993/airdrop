from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import requests
from bs4 import BeautifulSoup



class Near():

    def createWalletAndWriteToFile(self):
        i = 1
        f = open("examp.le", "w", encoding='utf-8')
        while (i < 100):
            f.write(
                f'Название кошелька: ukrlindan{i}\n\nСекретная фраза:secret pharse\n_____________________________________\n\n')
            i = i + 1
        f.close()
    def parseNumberOfSecretPharse(self,url):
        self.openSite(url)
        print(f'try open page:{url}')
        page = requests.get(url)
        print(f'response code:{page.status_code}')
        soup = BeautifulSoup(page.text, "html.parser")
        wallet_number=soup.findAll('div')[0]
        print(soup)


    def openBrowser(self):
        global driver
        chrome_options = Options()
        # chrome_options.add_extension('')
        driver = webdriver.Chrome(executable_path='..\chromedriver.exe', chrome_options=chrome_options)

        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w')
        driver.maximize_window()
        time.sleep(10)
        print('add metamask to chrome toolbar')

    def openSite(url):
        driver.get('https://wallet.near.org/setup-seed-phrase/ukrlindan1.near/verify')



near = Near()
near.parseNumberOfSecretPharse('https://wallet.near.org/setup-seed-phrase/ukrlindan1.near/verify')






























