from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")
time.sleep(2)

quotes_elements = driver.find_elements(By.CLASS_NAME, "quote")

quotes_list = []
authors_list = []
book_names_list = []

for element in quotes_elements:
    quote_text = element.find_element(By.CLASS_NAME, "text").text
    author_name = element.find_element(By.CLASS_NAME, "author").text
    book_name = element.find_element(By.CLASS_NAME, "keywords").text if element.find_elements(By.CLASS_NAME, "keywords") else "Not available"
    
    quotes_list.append(quote_text)
    authors_list.append(author_name)
    book_names_list.append(book_name)

df = pd.DataFrame({
    "Quote": quotes_list,
    "Author": authors_list,
    "Book Name": book_names_list
})

df.to_excel("scraped_quotes_extended.xlsx", index=False)

driver.quit()
