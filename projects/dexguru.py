def swapNativeToken():
    print('переключаюсь на вкладку dex.guru')
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/main/div/div/div[2]/div/div[1]/section/div[1]/div[2]/div/div[2]/input').send_keys(
        '0.05')
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/main/div/div/div[2]/div/div[1]/section/div[3]/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[4]/div/div[1]/button/span').click()
    time.sleep(5)
    print('переключаюсь на вкладку metamask для подтверждения обмена')
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[3]/div[3]/footer/button[2]').click()


