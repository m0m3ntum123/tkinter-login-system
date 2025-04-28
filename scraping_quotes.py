from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")
time.sleep(2)

quotes_elements = driver.find_elements(By.CLASS_NAME, "text")

quotes_list = []
for element in quotes_elements:
    quote_text = element.text
    quotes_list.append(quote_text)

df = pd.DataFrame({
    "Quotes": quotes_list
})

df.to_excel("scraped_quotes.xlsx", index=False)

driver.quit()
