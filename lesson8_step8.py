from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH,"//input[@name='firstname']")
    input1.send_keys("Smolensk")
    input2 = browser.find_element(By.XPATH,"//input[@name='lastname']")
    input2.send_keys("Smoll")
    input3 = browser.find_element(By.XPATH,"//input[@name='email']")
    input3.send_keys("Eensk@mail.kz")
    import os 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element = browser.find_element(By.XPATH,"//input[@id='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)


finally:
    time.sleep(10)
    browser.quit()