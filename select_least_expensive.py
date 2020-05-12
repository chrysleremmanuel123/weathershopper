"""
Learn to click a button with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2


SCOPE:
1) Launch Chrome driver
2) Navigate to weathershopper.pythonanywhere.com/moisturizer
3) Find the xpath for the 2 least expensive Moisturizers 1 with aloe and other almond
4) Find the Xpath for the cart button and perform click action
5) Check if all the items are selected from the cart are correct
6) Close the driver
"""
"""
1. Goto /moisturizers page
2. Add the least expensive aloe and least expensive almond
3. To the cart
"""
from selenium import webdriver
import time
#Create the instance of the webdreiver
browser = webdriver.Chrome()
#Navigate the URL
browser.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(5)
#Condidtion to add moisturizer
all_condition = ['aloe','almond']
def get_all_product(each_condition,all_products):
    "get the product name and price"
    min_price = 10000
    for each_product in all_products:
        each_product_text = each_product.text
        product_name = each_product_text.splitlines()[0]
        if each_condition in product_name.lower():
            get_product_price = each_product_text.splitlines()[1]
            get_product_price = int(get_product_price.split(" ")[-1])
            if min_price >= get_product_price:
                min_price = get_product_price
                min_product_name = product_name
    print("aloe",min_product_name,min_price)
    time.sleep(5)
    min_product_name=browser.find_element_by_xpath("//div[contains(@class,'col-4') and contains (.,'%s')]/descendant::button[text()='Add']"%(min_product_name)).click()
#Find the xpath for all the products 
all_products = browser.find_elements_by_xpath("//div[contains(@class,'col-4')]")
for each_condition in all_condition:
    get_all_product(each_condition,all_products)
