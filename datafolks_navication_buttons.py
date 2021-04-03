#Verify the text of all navigation buttons in the top right corner (Home, Portfolio, Services, Contact Us)

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.datafolks.com")

#code for home button
home_button = driver.find_element_by_xpath("//div[@data-elem-id=1551634462374]")
assert home_button.text == "Home"

#code for portfolio button
portfolio_button = driver.find_element_by_xpath("//div[@data-elem-id='1551634481382']")
assert portfolio_button.text == "Portfolio"

#code for services button
services_button = driver.find_element_by_xpath("//div[@data-elem-id = 1551634484712]")
assert services_button.text == "Services"

#code for Contact Us button
contact_us = driver.find_element_by_xpath("//div[@data-elem-id =1551634487768]")
assert contact_us.text == "Contact Us"

driver.quit()