from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 1. Configure Chrome to run without a window (Headless)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # 3. Navigate to the Login Form
    driver.get("https://the-internet.herokuapp.com")
    print(f"Page Title: {driver.title}")

    # 4. Find elements and input data
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # 5. Submit the form
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    # 6. Verify success
    success_msg = driver.find_element(By.ID, "flash").text
    print(f"Result: {success_msg}")

finally:
    driver.quit()
