# tested website"https://www.seleniumeasy.com/test/basic-first-form-demo.html"
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

driver.find_element(By.ID, "sum1").send_keys(5)

driver.find_element(By.ID, "sum2").send_keys(10)

driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button").click()

time.sleep(10)

driver.quit()
