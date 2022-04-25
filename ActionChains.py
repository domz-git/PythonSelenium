from multiprocessing import Value
import time
from turtle import color
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\SeleniumDrivers\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookieCount = driver.find_element_by_id("cookies")
firstUpgrade = driver.find_element_by_id("productPrice0")
secondUpgrade = driver.find_element_by_id("productPrice1")
thirdUpgrade = driver.find_element_by_id("productPrice2")

actions = ActionChains(driver)


while True:
    cookie.click()
    count = int(cookieCount.text.split(" ")[0])

    upgradeFirst = ActionChains(driver)
    upgradeFirst.move_to_element(firstUpgrade)
    valueFirst = int(firstUpgrade.text)
    upgradeFirst.click()

    upgradeSecond = ActionChains(driver)
    upgradeSecond.move_to_element(secondUpgrade)
    valueSecond = int(firstUpgrade.text)
    upgradeSecond.click()

    upgradeThird = ActionChains(driver)
    upgradeThird.move_to_element(thirdUpgrade)
    valueThird = int(firstUpgrade.text)
    upgradeThird.click()

    if valueThird < count:
        upgradeThird.perform()
    if valueSecond < count:
        upgradeSecond.perform()
    if valueFirst < count:
        upgradeFirst.perform()