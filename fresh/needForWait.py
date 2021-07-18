from selenium import webdriver
import time

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("http://www.seleniumframework.com/Practiceform/")

element = driver.find_element_by_id("periodicElement")

time.sleep(2)

print(element.text)


driver.quit()
