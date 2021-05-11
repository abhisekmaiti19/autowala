#============>Filling out form by selenium<================
#https://www.seleniumeasy.com/test/basic-first-form-demo.html
#using byclass

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

driver.find_element(By.ID,"user-message").send_keys("hello")
# dirver.find_element(By.CLASS_NAME,"btn btn-default").click() will raise an exception
# the reason is in the class name if there is a space then the selenium consider there are more than one class name is typed, and this is not a syntax
#better way is cought XPATH 

driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button").click()
time.sleep(10)
driver.quit()
