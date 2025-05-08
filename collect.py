from bs4 import BeautifulSoup
import os
import pandas as pd
import re


# Lists to store data
product_links = []
product_names = []
product_prices = []

data_dir = "data"

files = os.listdir(data_dir)


# Process each file
for file in files: 
    file_path = os.path.join(data_dir, file)

    with open(file_path, 'r', encoding='utf-8') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    link_element = soup.find(class_="CGtC98")

    full_link = "https://www.flipkart.com" + link_element['href']
    product_links.append(full_link)
    
    name_element = soup.find(class_="KzDlHZ")
    product_names.append(name_element.text.strip())
    
    # Extract price
    price_element = soup.find(class_=re.compile("Nx9bqj.*_4b5DiR"))  # Added closing parenthesis
    price_text = price_element.text.strip()
    product_prices.append(price_text)

df = pd.DataFrame({
    'Product Name': product_names,
    'Price': product_prices,
    'Product Link': product_links
})

# Save to Excel
excel_file = 'laptop_data.xlsx'
df.to_excel(excel_file, index=False)
print(f"\nData saved")

print(f"\nTotal products: {len(df)}")