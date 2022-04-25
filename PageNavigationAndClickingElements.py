import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\SeleniumDrivers\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.w3schools.com")

try:
    linkOne = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "accept-choices"))
    )
    linkOne.click()
    time.sleep(1)
    linkOne = driver.find_element_by_link_text("Not Sure Where To Begin?")
    linkOne.click()
finally:
    time.sleep(1)

try:
    linkOne = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Learn HTML"))
    )
    linkOne.click()
finally:
    i=0
    while i<2:
        driver.back()
        i+=1
    time.sleep(3)