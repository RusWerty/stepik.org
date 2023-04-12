from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.XPATH,"//*[@class='btn btn-primary']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
               
    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.XPATH,"//*[@id='input_value']")
    x = x_element.text
    y = calc(int(x))
    input1 = browser.find_element(By.XPATH,"//*[@id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    button = browser.find_element(By.XPATH,"//*[@class='btn btn-primary']")
    button.click()
    time.sleep(5)
    
finally:
    time.sleep(10)
    browser.quit()