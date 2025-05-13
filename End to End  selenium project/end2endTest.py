import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
time.sleep(10)
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    product_name = product.find_element(By.XPATH,"div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class = 'btn btn-success']").click()

print("hello")



time.sleep(100)