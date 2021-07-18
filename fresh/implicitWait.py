# implicit waits

# an implicit wait tells webDriver to poll the DOM a crtain amount of time when
# tying to find element(or element) not immedietly available . The default setting is 0. Once set,
# the implicit wait is set for the life of the Web Driver object.in

# ---------------------------------------------------------------------------------------------------

# from selenium import webdriver
# import time

# driver = webdriver.Chrome("../chromedriver.exe")

# driver.get("http://www.seleniumframework.com/Practiceform/")

# element = driver.find_element_by_id("periodicElement")

# time.sleep(2)

# print(element.text)


# driver.quit()


# -------------------------------------------------------------------------------
from selenium import webdriver
import time

driver = webdriver.Chrome("../chromedriver.exe")
start_time = time.time()
# driver.implicitly_wait(5)
driver.get("http://www.seleniumframework.com/Practiceform/")
time.sleep(5)
element = driver.find_element_by_id("periodicElement")
print("exact time:", time.time() - start_time)
print(element.text)
driver.quit()
