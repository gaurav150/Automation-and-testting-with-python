import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# Wait for the element to be clickable before clicking
wait = WebDriverWait(driver, 10)
forgot_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Forgot password?")))
forgot_link.click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("gauravara24@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(50)