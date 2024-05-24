import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to type text slowly with random delay
def type_slowly(element, text, min_delay=0.05, max_delay=0.2):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))

# Set up the WebDriver (ensure ChromeDriver is in your PATH or provide the path to ChromeDriver)
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Find the search box using its name attribute value
    search_box = driver.find_element("name", "q")
    
    # Enter the search query and send the return key
    search_query = "youtube.com"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results to load
    time.sleep(2)
    
    # Find the first search result link and click it
    first_result = driver.find_element("xpath", "(//h3)[1]/ancestor::a")
    first_result.click()
    
    # Wait for the page to load
    time.sleep(2)
    
    # Print the current URL to verify the click
    print(f"Current URL: {driver.current_url}")
    
    # Find the first button using its XPath and click it
    first_button = driver.find_element("xpath", "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
    first_button.click()

    # Wait for the button action to complete
    time.sleep(2)
    
    # Find the second button using its XPath and click it
    second_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button/span")
    second_button.click() 
    
    # Find the third button using its XPath and click it
    third_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[3]")
    third_button.click()

    # Wait for the button action to complete
    time.sleep(2)

    # Find the first input field using its XPath, click it, and type "first name" slowly with random delay
    first_name_field = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/input")
    first_name_field.click()
    type_slowly(first_name_field, "first name")

    # Add a small delay
    time.sleep(2)

    # Find the second input field using its XPath, click it, and type "lastname" slowly with random delay
    last_name_field = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/input")
    last_name_field.click()
    type_slowly(last_name_field, "lastname")

    # Add a small delay
    time.sleep(2)

    # Find the next button using its XPath and click it
    next_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button/span")
    next_button.click()

    # Add some delay to observe the effect
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
