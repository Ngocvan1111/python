import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()

url = 'https://www.geeksforgeeks.org/'
url2 = 'https://stackoverflow.com/questions/29092970/importerror-cannot-import-name-webdriver'

# get geeksforgeek.org
driver.get(url)
driver2.get(url2)
# get element
# element = driver.find_element(By.CLASS_NAME, "ant-input-lg")
# element = driver.find_element(By.NAME, "search")
# element2 = driver2.find_element(By.CLASS_NAME, "s-input")
element2 = driver2.find_element(By.NAME, "q")

# element.send_keys("Arrays")
# print(element)
element2.send_keys("HELLO WORLD")
element2.submit()
time.sleep(60)
