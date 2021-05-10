from selenium import webdriver
import time


driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")

button = driver.find_element_by_id("save")


for i in range(5):
	button.click()
	time.sleep(5)
	details = driver.find_elements_by_id("loading")
	print(details[0].text)
	

driver.quit()