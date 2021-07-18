from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.flipkart.com"

driver.get(url)
time.sleep(2)


driver.get("https://codediksha.com")
time.sleep(2)


driver.refresh()
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

driver.close()
