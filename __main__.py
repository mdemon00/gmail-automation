from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (ensure ChromeDriver is in your PATH or provide the path to ChromeDriver)
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Find the search box using its name attribute value
    search_box = driver.find_element("name", "q")
    
    # Enter the search query and send the return key
    search_query = "gmail.com"
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
    first_button = driver.find_element("xpath", "/html/body/header/div/div/div/details/summary/div[1]")
    first_button.click()

    # Wait for the button action to complete
    time.sleep(2)
    
    # Find the second button using its XPath and click it
    second_button = driver.find_element("xpath", "/html/body/header/div/div/div/details/div/a[1]")
    second_button.click()

    # Add some delay to observe the effect
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
