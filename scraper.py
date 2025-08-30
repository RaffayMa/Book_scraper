from bs4 import BeautifulSoup

with open("file.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

# goal for this script get each product title, price and availability

for price in soup.find_all(class_='price_color'):
    p = price
    print(p.text)

for avail in soup.find_all(class_='instock availability'):
    a = avail
    print(a.text)


# Problem the data is being extracted seperately need to create and access a single book obj print title, price and availablity