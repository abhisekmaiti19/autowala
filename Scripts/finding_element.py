# ---------------------------finding elements---------------------------
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.google.com")
time.sleep(2)

def autom(count):
	while count<10:

		textfield = driver.find_element_by_name("q")

		textfield.send_keys("hello world" + Keys.RETURN)
		time.sleep(2)

		home_button = driver.find_element_by_id("logo")
		home_button.click()

		count += 1 
autom(0)


driver.quit()
