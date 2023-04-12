from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH,"//input[@class='form-control first']")
    input1.send_keys("Smolensk")
    input2 = browser.find_element(By.XPATH,"//input[@class='form-control second']")
    input2.send_keys("Smoll")
    input3 = browser.find_element(By.XPATH,"//input[@class='form-control.third' and @placeholder='Input.your.email']")
    input3.send_keys("Eensk@mail.kz")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)

    welcome_text_elt = browser.find_element(By.XPATH, "//h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()