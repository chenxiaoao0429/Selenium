#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))
#email_element=driver.find_element_by_id("register_email")
#print(driver.find_element_by_id("register_email").get_attribute("placeholder"))
driver.find_element_by_id("register_email").send_keys("chenao@163.com")
print(driver.find_element_by_id("register_email").get_attribute("value"))

time.sleep(5)

driver.close()


