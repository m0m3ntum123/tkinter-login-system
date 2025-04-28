from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_nkw=laptop")
time.sleep(2)

product_elements = driver.find_elements(By.CLASS_NAME, "s-item")

product_names = []
prices = []
descriptions = []

for element in product_elements:
    try:
        product_name = element.find_element(By.CLASS_NAME, "s-item__title").text
    except:
        product_name = "Not available"
    
    try:
        price = element.find_element(By.CLASS_NAME, "s-item__price").text
    except:
        price = "Not available"
    
    try:
        description = element.find_element(By.CLASS_NAME, "s-item__description").text
    except:
        description = "Not available"
    
    product_names.append(product_name)
    prices.append(price)
    descriptions.append(description)

df = pd.DataFrame({
    "Product Name": product_names,
    "Price": prices,
    "Description": descriptions
})

df.to_excel("scraped_ebay_products.xlsx", index=False)

driver.quit()
