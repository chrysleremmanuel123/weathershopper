from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL
driver.get("https://weathershopper.pythonanywhere.com/")

# Check if the title of the page is proper
if(driver.title=="Current Temperature"):
    print ("Success")
else:
    print ("Failure")

# Find the name field using xpath with id
current_temp= driver.find_element_by_xpath("//span[@id='temperature']")
current_temp=current_temp.text
current_temp=current_temp.split()[0]

def testpassed():
    "To check if the page is landed on the correct site"
    if(driver.title=="The Best Sunscreens in the World!" or driver.title=="The Best Moisturizers in the World!"):
        print("Correct site")
    else:
        print("wrong site")

#check temp is below 19 or not
if(int(current_temp)<=19):
    buy_mostiruzer=driver.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]")
    buy_mostiruzer.click()
    testpassed()
    
else:
    buy_sunscreen=driver.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]")
    buy_sunscreen.click()
    testpassed()
 

driver.close() 