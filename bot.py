import pyautogui
import time
from selenium import webdriver
import os

code22 = int(input("Game code: "))
botnum = int(input("Number of bots: "))
listname = input("txt file to use: ")

cwd = os.getcwd()
chromedriverdir = f'{cwd}/webdrivers/chromedriver86.exe'
url = 'https://www.gimkit.com/live/'

driver = webdriver.Chrome(chromedriverdir)
driver.implicitly_wait(5)
driver.get(url)
time.sleep(2)
tab = 1
#---IGNORE COMMENTED OUT CODE FOR NOW. IT WILL BE USED LATER---#
#nume = 9
# timeouttab = 100000


namelist = open(f'{listname}.txt', 'r')



while botnum > 0:
    #while tab != nume:
        name = namelist.readline()
        time.sleep(0.5)
        #---Input game code and submit---#
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[2]/div/div/div/div/form/input').send_keys(code22)
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[2]/div/div/div/div/div').click()
        
        #---Input name and submit---#
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[2]/div/div/div/div/form/input').send_keys(name)
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[2]/div/div/div/div/div').click()

        time.sleep(0.5)
        #---Open a new window with javascript and focus on that window---#
        driver.execute_script(f"window.open({url})")
        driver.switch_to.window(driver.window_handles[tab])

        #---Count how many bots and tabs are open---#
        botnum = botnum - 1
        print (tab)
        tab = tab + 1      

        #---Delete cookies---#
        driver.delete_cookie
    # time.sleep(60)
    # nume = nume + timeouttab