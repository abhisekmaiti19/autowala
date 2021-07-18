# tested website"https://www.seleniumeasy.com/test/basic-first-form-demo.html"
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

mesage = "hello world"

driver.find_element(By.ID, "user-message").send_keys(mesage)
# driver.find_element(By.CLASS_NAME,"btn btn-default").click() raise error due to space between in classname

driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button").click()

dis_messege = driver.find_element(By.ID, "display")
time.sleep(5)

# assert mesage == dis_messege


driver.quit()
