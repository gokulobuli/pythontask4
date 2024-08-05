from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver (Chrome in this case)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the Instagram profile URL
    driver.get('https://www.instagram.com/guviofficial/')

    # Wait for the page to load and elements to be present
    wait = WebDriverWait(driver, 10)

    # Locate the followers and following counts using XPath
    followers_count = driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]/span/span').text

    following_count = driver.find_element(By.XPATH, '//a[contains(@href, "/following/")]/span/span').text

    # Print the extracted follower and following counts
    print(f"Followers Count: {followers_count}")
    print(f"Following Count: {following_count}")

finally:
    # Ensure the WebDriver quits
    driver.quit()
