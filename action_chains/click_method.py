import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "https://www.geeksforgeeks.org/"

driver.get(url)

element = driver.find_element(By.LINK_TEXT, "Python")

action = ActionChains(driver)

# action.click(on_element = element)
action.click_and_hold(on_element=element)

action.perform()

time.sleep(60)
