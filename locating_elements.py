from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Make sure the data directory exists
if not os.path.exists("data"):
    os.makedirs("data")

driver = webdriver.Chrome()
query = 'laptop'

for i in range(1, 21):
    try:
        # Navigate to the page
        driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
        
        # Wait until at least one product card is present (up to 10 seconds)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "CGtC98"))
        )
        
        # Get all laptop elements on the page - not just the first one
        elements = driver.find_elements(By.CLASS_NAME, "CGtC98")
        print(f"Found {len(elements)} laptops on page {i}")
        
        # Save each laptop element to a separate file
        for idx, elem in enumerate(elements):
            with open(f"data/{query}_page{i}_item{idx+1}.html", "w", encoding="utf-8") as file:
                file.write(elem.get_attribute("outerHTML"))
        
    except Exception as e:
        print(f"Error on page {i}:", e)

    # Add a delay to avoid overloading the server
    time.sleep(3)

driver.quit()