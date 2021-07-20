# alert

from selenium import webdriver
import time

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div[2]/div[2]/button').click()

alert = driver.switch_to_alert()

alert.dismiss()
time.sleep(3)

ccbjsjcb

driver.quit()
