# //handle javascrip

from selenium import webdriver
import time

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

time.sleep(5)
script = 'document.getElementById("user-message").value = "Hello World";'

driver.execute_script(script)

driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button').click()

time.sleep(5)

driver.quit()
