# and submit form
#Verify returning to the home page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

def verifyLogo():
   # wait until logo on the page is visible and verify its text
   logo = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"tn-atom")))
   assert logo.text == "DATAFOLKS"

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.datafolks.com")

verifyLogo()

# wait until Contact Us Button in Navigation bar is clickable and Click on "Contact Us" button
contact_us_home_btn = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[13]/a")))
contact_us_home_btn.click()

#Fill in input field for name
name_input_field = WebDriverWait(driver, 40).until((EC.visibility_of_element_located((By.NAME, "Name"))))
name_input_field.send_keys("Josh Traverson")

#Fill in input field for email
name_input_field = WebDriverWait(driver, 40).until((EC.visibility_of_element_located((By.NAME, "Email"))))
name_input_field.send_keys("testemail@joshtraverson.com")

#Fill in input field for name phone number
phone_input_field = WebDriverWait(driver, 40).until((EC.visibility_of_element_located((By.NAME, "Phone"))))
phone_input_field.send_keys("+180973780098")

#Fill in input field for name country
phone_input_field = WebDriverWait(driver, 40).until((EC.visibility_of_element_located((By.NAME, "Country"))))
phone_input_field.send_keys("Ukraine")

#find send button and submit form
send_btn = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/button")))
send_btn.click()

#wait until Close icon bar is clickable
close_btn = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[17]/div/div/div[1]/div")))
close_btn.click()

verifyLogo()

driver.quit()