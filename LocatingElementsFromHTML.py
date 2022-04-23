import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\SeleniumDrivers\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.w3schools.com")
search = driver.find_element_by_id("search2")
search.send_keys("html")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sidenav"))
    )
    articleLinks = main.find_elements_by_tag_name("a")
    for article in articleLinks:
        print(article.text)
finally:
    time.sleep(5)