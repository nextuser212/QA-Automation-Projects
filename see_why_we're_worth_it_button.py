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

# wait until Contact Us in Navigation bar is clickable
see_shy_worth_btn = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[11]/a/u")))
see_shy_worth_btn.click()

# verify that Mobile Development area of expertise shown
mob_dev_header = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[6]/div/div/div[7]')))
assert mob_dev_header.text == "Mobile Development"

# verify that Web Development area of expertise shown
web_dev = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[6]/div/div/div[5]')))
assert web_dev.text == "Web Development"

# verify that  Augmented Reality area of expertise shown
Augmented_Reality = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[6]/div/div/div[6]')))
assert Augmented_Reality.text == "Augmented Reality"

# verify that Virtual_Reality area of expertise shown
Virtual_Reality = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[6]/div/div/div[4]')))
assert Virtual_Reality.text == "Virtual Reality"

driver.quit()