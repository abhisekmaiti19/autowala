from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

checkbox = driver.find_element(By.ID, "isAgeSelected")

print("Before clicking:", checkbox.is_selected())

time.sleep(1)
checkbox.click()

print("After Clicking:", checkbox.is_selected())

time.sleep(5)


driver.quit()
