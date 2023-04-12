from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
               
    import math

    def calc(z):
        return str(int(x) + int(y))
    
    x_element = browser.find_element(By.XPATH,"//*[@id='num1']")
    x = x_element.text
    y_element = browser.find_element(By.XPATH,"//*[@id='num2']")
    y = y_element.text
    z = calc(int(x))
    input1 = browser.find_element(By.XPATH,"//*[@id='dropdown']")
    input1.send_keys(z)
    button = browser.find_element(By.XPATH,"//*[@class='btn btn-default']")
    button.click()
    time.sleep(10)
    
finally:
    time.sleep(10)
    browser.quit()