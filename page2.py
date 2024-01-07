from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


webdriver_path = '/home/alokie/Downloads/chromedriver'
# Update to the correct path
# Path to the Chrome WebDriver


# Set up the Chrome WebDriver instance in headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://in.lining.studio/category/badminton/rackets/attacking")

# Wait for the page to load (you may need to customize the wait time)
driver.implicitly_wait(10)

# Function to scroll down the page


def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust sleep time as needed


# Get the initial page source after interacting with the website
page_source = driver.page_source

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(page_source, "html.parser")

# Find all elements with the specified CSS selector
elements = driver.find_elements(By.CLASS_NAME,
                                "cursor-pointer rounded-sm px-3 py-2 text-sm sm:text-lg text-gray-50").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located(
    (By.XPATH, "//h1[@class='new-page-header']")))

# Get the updated page source
new_page_source = driver.page_source

# Use BeautifulSoup to parse the HTML of the new page
soup = BeautifulSoup(new_page_source, "html.parser")

# Find all elements with the specified CSS selector
elements = driver.find_elements(By.CLASS_NAME,
                                "text-sm.font-semibold.leading-snug.text-black.md:text-base")


# Print the text content of each element
for element in elements:
    print(element.text)

# Scroll down and load more content
scroll_down()

# Find elements again after scrolling
elements_after_scroll = driver.find_elements(By.CLASS_NAME,
                                             "text-sm.font-semibold.leading-snug.text-black.md:text-base")


i = 0
# Print the text content of the additional elements
for element in elements_after_scroll:
    i += 1
    print(element.text)

print(i)
# Close the WebDriver
driver.quit()
