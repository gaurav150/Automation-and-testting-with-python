import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
browserSortedVeggies = []
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
wait = WebDriverWait(driver, 10)
wait.until(ec.presence_of_element_located((By.XPATH, "//span[text()='Veg/fruit name']"))).click()

browserVegName = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in browserVegName:
    browserSortedVeggies.append(ele.text)
original_sorted_list = browserSortedVeggies.copy()
browserSortedVeggies.sort()
assert  browserSortedVeggies == original_sorted_list
time.sleep(100)