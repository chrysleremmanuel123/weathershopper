"""
Learn to click a button with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2


SCOPE:
1) Launch Chrome driver
2) Navigate to weathershopper.pythonanywhere.com/moisturizer
3) Find the xpath for all the 6 add buttons and perform click action on all 6 buttons
4) Finf the Xpath for the cart button and perform click action
5) Check if all the items are selected from the cart
6) Close the driver
"""
import time
from selenium import webdriver
# Create an instance of Chrome WebDriver
browser = webdriver.Chrome()
# KEY POINT: The driver.get method will navigate to a page given by the URL
browser.get('https://weathershopper.pythonanywhere.com/moisturizer')
# Find the button field using xpath with class
add_button = browser.find_elements_by_xpath("//button[@class='btn btn-primary']")
#Run for loop for 6 buttons
for each_button in add_button:
    each_button.click()
# Find the cart field using xpath with class
cart_button = browser.find_element_by_xpath("//button[@class='thin-text nav-link']")
cart_button.click()
#count the number of items present in cart
rows= browser.find_elements_by_xpath("//table[@class='table table-striped']/tbody/tr")
print(len(rows))
# Pause the script for 10 sec 
time.sleep(10)
# Quit the browser window
browser.close() 
