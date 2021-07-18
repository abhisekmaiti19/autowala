from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# for usng keys

driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://google.com")

textField = driver.find_element_by_name("q")
textField.send_keys("Hello world" + Keys.RETURN)
# mentioned above line just do -> first search for if any element name in Google.com that is "q", if found the pass the text "Hell World" and Keys.RETURN do the same as click Enter in keyboard

# finding element in a webpage
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_lisk_text
# find_element_by_tag_name
# find_element_by_class_name

# find_element_by_css_selector
# find_element_by_name
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector


time.sleep(2)


driver.quit()
