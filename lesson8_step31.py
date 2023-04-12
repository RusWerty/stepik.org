from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    wait = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.XPATH,"//*[@id='price']"),'$100')
        )
    button = browser.find_element(By.XPATH,"//*[@id='book']")
    button.click()
      
    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.XPATH,"//*[@id='input_value']")
    x = x_element.text
    y = calc(int(x))
    input1 = browser.find_element(By.XPATH,"//*[@id='answer']")
    input1.send_keys(y)
    button = browser.find_element(By.XPATH,"//*[contains(text(), 'Submit')]")
    button.click()
    time.sleep(5)
    
finally:
    time.sleep(10)
    browser.quit()
    