# so what is Element0
#Task
#the task is -> Fnd and print "Element0" from the website given below?
#http://www.seleniumframework.com/practiceform/

#-----------Common Case for waits ---------------

# from selenium import webdriver
# import time

# driver = webdriver.Chrome("../chromedriver.exe")

# driver.get("http://www.seleniumframework.com/practiceform/")

# mytext = driver.find_element_by_id("periodicElement")

#timesleep(5)
# print(mytext.text)

# driver.quit()

#-------------Implicits Waits--------------------

# from selenium import webdriver
# driver = webdriver.Chrome("../chromedriver.exe")

# driver.get("http://www.seleniumframework.com/practiceform/")

# driver.implicitly_wait(5)#second

# mytext = driver.find_element_by_id("periodicElement")

# print(mytext.text)

# driver.quit()

#--------Better Understanding of implicit waits--------------

from selenium import webdriver
import time 

driver = webdriver.Chrome("../chromedriver.exe")

start_time = time.time()
driver.get("http://www.seleniumframework.com/practiceform/")

# time.sleep(5)

driver.implicitly_wait(5)#second

mytext = driver.find_element_by_id("periodicElement")

print("exact time:",time.time()-start_time)

driver.quit()