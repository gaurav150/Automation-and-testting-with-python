import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
options = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
time.sleep(5)
print(len(options))
for option in options:
    if option.get_attribute("value") == "option2":
        option.click()
        assert option.is_selected()
        break

radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
time.sleep(5)
# for button in radio_buttons:
#     if button.get_attribute("value") == "radio2":
#         button.click()
#         assert button.is_selected()
#         break
radio_buttons[1].click()
assert radio_buttons[1].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(1000)