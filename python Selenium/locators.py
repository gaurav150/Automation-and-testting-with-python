

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
## ID ,Xpath, CSSSelector, Classname, name, linkText

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,'exampleInputPassword1').send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

# to create xpath we have to write like
# //tagname[@attribute='value]
# CSS tagname[attribute='value]  ,#id, .classname
## //input[@type='submit']

driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("pratuysh")
driver.find_element(By.CSS_SELECTOR,"input[value='option1']").click()

## select class for static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello Again")
time.sleep(50)