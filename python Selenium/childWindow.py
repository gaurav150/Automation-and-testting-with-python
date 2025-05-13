import time

from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
print(windowsOpened)
time.sleep(50)
driver.close()
# action = ActionChains(driver)