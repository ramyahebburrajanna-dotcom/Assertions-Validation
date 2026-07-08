from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome Browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Maximize browser window
driver.maximize_window()

# Open SauceDemo website
driver.get("https://www.saucedemo.com")

# -------------------------------
# Step 1: Login
# -------------------------------

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# -------------------------------
# Step 2: Assert URL
# -------------------------------

assert "inventory" in driver.current_url

print("✅ URL Assertion Passed")

# -------------------------------
# Step 3: Assert Page Title
# -------------------------------

page_title = driver.find_element(By.CLASS_NAME, "title").text

assert page_title == "Products"

print("✅ Page Title Assertion Passed")

# -------------------------------
# Step 4: Add Product to Cart
# -------------------------------

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

cart_badge = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
).text

print("Cart Badge:", cart_badge)

assert cart_badge == "1"

print("✅ Cart Badge Assertion Passed")

time.sleep(2)


# -------------------------------
# Step 5: Open Cart
# -------------------------------

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

time.sleep(2)

# -------------------------------
# Step 6: Assert Product Name
# -------------------------------

product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

assert product_name == "Sauce Labs Backpack"

print("✅ Product Assertion Passed")

print("\n🎉 All Assertions Passed Successfully!")

driver.quit()