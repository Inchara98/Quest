from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the WebDriver with the configured options
driver = webdriver.Chrome(options=chrome_options)

# Perform your tests here...
driver.get("https://example.com")
print(driver.title)

# Close the WebDriver
driver.quit()

