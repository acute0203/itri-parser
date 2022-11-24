import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="geckodriver")

driver.maximize_window()

driver.get("http://qxf2.com/selenium-tutorial-main")
time.sleep(2)


name = driver.find_element(By.XPATH, "//input[@id='name']")
#name = driver.find_element_by_xpath("//input[@id='name']")  

name.send_keys('Avinash')
time.sleep(3)

driver.find_element(By.XPATH, "//input[@name='email']").send_keys('avinash@qxf2.com')
#driver.find_element_by_xpath("//input[@name='email']").send_keys('avinash@qxf2.com')


phone = driver.find_element(By.ID, 'phone')
#phone = driver.find_element_by_id('phone')
phone.send_keys('9999999999')
time.sleep(3)


button = driver.find_element(By.XPATH, "//button[text()='Click me!']")
#button = driver.find_element_by_xpath("//button[text()='Click me!']")  
button.click()

time.sleep(3)

if (driver.current_url== 'https://qxf2.com/selenium-tutorial-redirect'):
    print("Success")
else:
    print("Failure")

# Close the browser   
#driver.close()


