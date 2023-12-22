from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# website url
url = 'https://www.instagram.com'

# Opening web browser
browser = webdriver.Edge()  # Here Microsoft Edge is selected
browser.get(url)

# Wait 4 sec to let the page load
time.sleep(2)

# Password declared in a variable
password = "<Your Password>"

# Username input
browser.find_element(By.NAME, 'username').send_keys('<Your Username>')

# Password input
browser.find_element(By.NAME, 'password').send_keys(password)

# Click on login button
WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button'))).click()

time.sleep(4)

# Logout menu
WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a'))).click()

# Clicking on logout button
time.sleep(2)
WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[8]/div[1]'))).click()

# Wait 5 secs after logout and close browser
time.sleep(5)
browser.close()
