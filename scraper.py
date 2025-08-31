from bs4 import BeautifulSoup

with open("file.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

# goal for this script get each product title, price and availability
# Create and access a single book obj print title, price and availablity

for cont in soup.find_all('li'):
    book = cont.find(class_="product_pod")
    if book:
        title = book.h3.a['title']
        pp = book.find(class_="price_color").text
        avail = book.find(class_="instock availability").text
    else :
        print("Error scraping book")

# Print extracted details
print(title)
print(pp)
print(avail)
print(" ")

# Problem only print last book details need to print all of the items/books in the page

