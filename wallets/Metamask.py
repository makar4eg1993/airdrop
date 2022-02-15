from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

# logging.basicConfig(filename='metamasklogger',
#                             filemode='a',
#                             format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                             datefmt='%H:%M:%S',
#                             level=logging.DEBUG)

class Metamask():

    def __init__(self,secret_pharse,password):
        self.password=password
        self.secret_pharse=secret_pharse

    # def getSecretPharse(self):
    #     print(self.secret_pharse)

    def test(self):
        print('test metamask')

    def openBrowser(self, extension_path, webdriver_path):
        global driver
        chrome_options = Options()
        chrome_options.add_extension(extension_path)
        driver = webdriver.Chrome(webdriver_path, chrome_options=chrome_options)

        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w')
        driver.maximize_window()
        time.sleep(10)
        print('add metamask to chrome toolbar')

    def pauseAndWaitEnter(self):
        programPause = input("Press the <ENTER> key to continue...")

    def enterToMetamask(self):
        driver.switch_to.window(driver.window_handles[0])
        try:
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/div/button').click()
        except Exception as ex:
            print(ex)
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button').click()
        except Exception as ex:
            # logging.error(ex)
            print(ex)
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/div/div[5]/div[1]/footer/button[1]').click()
        except Exception as ex:
            print(ex)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input').send_keys(self.secret_pharse)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="confirm-password"]').send_keys(self.password)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/button').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
        time.sleep(2)

    def openSiteInNewTab(url,tab_number):
        driver.execute_script("window.open('','_blank');")
        driver.switch_to.window(driver.window_handles[tab_number])
        driver.get(url)

    def swapInMetamask(self,swapfrom,swapto,summ):
        print('swap in metamask')

    def createAccaounts(self,count):
        i = 1
        driver.switch_to.window(driver.window_handles[0])
        while i < count:
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[2]/div').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div[6]/div[2]').click()
            time.sleep(3)
            i = i + 1
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div/div/div[2]/input').send_keys(f"abs{i}")
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div/div/div[2]/div/button[2]').click()
            print(i)

    def addBscNetwork(self):
        Metamask.openSiteInNewTab('https://bscscan.com/',1)
        time.sleep(7)
        driver.find_element_by_xpath('//*[@id="body"]/footer/div/div[1]/div[1]/div/div[2]/span/button').click()
        time.sleep(7)
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div/button[2]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/button[2]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
        time.sleep(5)

    def parseWalletAdress(self):
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div/div/div[1]/button').click()
        print('нажал на три точки ')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="popover-content"]/div[2]/button[1]/span').click()
        print('нажал на реквизиты счета ')
        time.sleep(3)
        body = driver.execute_script("return document.body.innerHTML") #вернуть html если динамическая страница
        bsoup = BeautifulSoup(body, 'html.parser')
        test = bsoup.find_all("input", class_="readonly-input__input")
        res = test[0]['value']
        print(res)
        f = open("walletsAddresses.txt", "w", encoding='utf-8')
        f.write(f'{res}\n')
        f.close()
        return res

    def dexguruSwap(self):
        print('начал свапать на dex.guru')
        Metamask.openSiteInNewTab('https://dex.guru/token/0xe9e7cea3dedca5984780bafc599bd69add087d56-bsc',2)
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div[10]/div/div[1]/a').click()
        driver.refresh()
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div/div/div[2]/div/div[1]/section/div[3]/button').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div[2]/div/div[1]/button').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        print('обновляю метамаск страницу для апрува на dex.guru')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
            time.sleep(5)
        except:
            pass
        time.sleep(7)
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[3]/button[2]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])


        print('переключаюсь на вкладку dex.guru для обратного свапа')
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(15)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div/div/div[2]/div/div[2]/section/div[1]/div[1]/div[2]/span').click()
        print('нажимаю макс сумму для обратного свопа')
        time.sleep(5)
        try:
            # если ранее свапали то делаем это
            driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/main/div/div/div[2]/div/div[2]/section/div[3]/button').click()
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[4]/div/div[1]/button').click()
            time.sleep(5)
        except:
            # если ранее не свапали то делаем это
            driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/main/div/div/div[2]/div/div[2]/section/div[3]/button').click()

        print('переключаюсь на вкладку metamask для апрува')
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[3]/footer/button[2]').click()
        print('переключаюсь на вкладку dex.guru для обмена')
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[3]/footer/button[2]')
        print('переключаюсь на вкладку metamask для апрува')
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[3]/div[3]/footer/button[2]').click()
        time.sleep(2)






