mport requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the e-commerce website to scrape
url = 'https://example-ecommerce-website.com/products'

# Fetch the HTML content of the website
response = requests.get(url)
html = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract product information
product_names = []
product_prices = []
product_ratings = []

# Assuming the website has specific classes for product name, price, and rating
for product in soup.find_all(class_='product'):
    name = product.find(class_='product-name').get_text(strip=True)
    price = product.find(class_='product-price').get_text(strip=True)
    rating = product.find(class_='product-rating').get_text(strip=True)
    
    product_names.append(name)
    product_prices.append(price)
    product_ratings.append(rating)

# Store the extracted data in a pandas DataFrame
data = {
    'Product Name': product_names,
    'Price': product_prices,
    'Rating': product_ratings
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('products.csv', index=False)

print("Data has been successfully scraped and saved to 'products.csv'.")



