from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
               
    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.XPATH,"//*[@id='treasure']")
    x = x_element.get_attribute('valuex')
    y = calc(int(x))
    input1 = browser.find_element(By.XPATH,"//*[@id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element(By.XPATH,"//*[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.XPATH,"//*[@id='robotsRule']")
    option2.click()
    button = browser.find_element(By.XPATH,"//*[@class='btn btn-default']")
    button.click()
    time.sleep(5)
    
finally:
    time.sleep(10)
    browser.quit()