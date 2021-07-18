# finding elements in a webpage (By Class)

# from selenium.webdriver.common.by import By
# driver.find_element_by_xpath('//button[text()="text description]')
# driver.find_element(By.XPATH,'//button[text()="some text"]')


#         By.ID
#         By.XPATH
#         By.LINK_TEXT
#         By.PARTIAL_LINK_TEXT
#         By.NAME
#         By.TAG_NAME
#         By.CLASS_NAME
#         By.CSS_SELECTOR

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")

for i in range(3):
    button = driver.find_element(By.ID, "save")
    button.click()
    time.sleep(5)
    details = driver.find_element(By.ID, "loading")
    print(details.text)

driver.quit()
