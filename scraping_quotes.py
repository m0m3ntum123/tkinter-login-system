from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def extract_product_info(element):
    """Extract product name, price, and description from a given product element."""
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
    
    return product_name, price, description

def categorize_product(product_name, description):
    """Categorize the product based on its name or description."""
    gpu_keywords = ['gpu', 'graphics card', 'video card', 'nvidia', 'rtx', 'gtx']
    cpu_keywords = ['cpu', 'processor', 'intel', 'amd', 'core i', 'ryzen']
    
    # Lowercase the product name and description for case-insensitive comparison
    product_name_lower = product_name.lower()
    description_lower = description.lower()
    
    if any(keyword in product_name_lower or keyword in description_lower for keyword in gpu_keywords):
        return 'GPU'
    elif any(keyword in product_name_lower or keyword in description_lower for keyword in cpu_keywords):
        return 'CPU'
    else:
        return 'Other'

def save_to_excel(data, filename):
    """Save the collected data to an Excel file."""
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def main():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    
    # Open eBay search page for laptops (or any other keyword related to GPUs, CPUs)
    driver.get("https://www.ebay.com/sch/i.html?_nkw=laptop")
    time.sleep(2)
    
    # Find all product elements on the page
    product_elements = driver.find_elements(By.CLASS_NAME, "s-item")
    
    # Prepare lists to store product data
    product_names = []
    prices = []
    descriptions = []
    categories = []
    
    # Loop through all product elements and extract the required information
    for element in product_elements:
        product_name, price, description = extract_product_info(element)
        category = categorize_product(product_name, description)
        
        # Append extracted data to respective lists
        product_names.append(product_name)
        prices.append(price)
        descriptions.append(description)
        categories.append(category)
    
    # Organize data into a dictionary for easy DataFrame creation
    data = {
        "Product Name": product_names,
        "Price": prices,
        "Description": descriptions,
        "Category": categories
    }
    
    # Save the data to an Excel file
    save_to_excel(data, "scraped_ebay_products_categorized.xlsx")
    
    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    main()
