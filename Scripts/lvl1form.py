from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

a,b = 10,20
total = a+b

driver.find_element(By.ID,"sum1").send(a)
driver.find_element(By.ID,"sum2").send(b)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button").click()



driver.quit()