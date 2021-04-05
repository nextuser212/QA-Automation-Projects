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

# find main text of home page and verify it's text
main_text = driver.find_element_by_xpath('//div[@data-elem-id=1551634856822]/h1')
assert main_text.text == "Quality code\nfor your ideas"

# wait until Contact Us in Navigation bar is clickable
contact_us_navigation_bar_btn = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Contact Us')]")))
contact_us_navigation_bar_btn.click()

verifyLogo()

# wait until text on the Contact Us page will be visible and verify its text
contact_page_header = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-elem-id=1551634856822]/h1')))
assert contact_page_header.text == "Get in touch"

#wait until email input field is visible and input mail@example.com
email_input_field = WebDriverWait(driver, 40).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("emailtet@gmail.com")

# wait until Submit bar is clickable
submit_bar_btn = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[10]/div[1]/form/div[2]/div[3]/button")))
submit_bar_btn.click()

#wait until Thank you text visible
thank_you_window = WebDriverWait(driver, 90).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="t-form-success-popup__wrapper"]')))
assert thank_you_window.text == "Thank you! We will contact you soon."

driver.quit()