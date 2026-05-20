import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("div", class_="quote")

data = []

# Extract data
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    data.append({
        "Quote": text,
        "Author": author
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("quotes.csv", index=False)

print("Data Saved Successfully!")