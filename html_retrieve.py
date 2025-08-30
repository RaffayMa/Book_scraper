import requests

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0"
}

r = requests.get(url, headers=headers)


if r.status_code == 200:
    with open("file.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("Sucess")
else:
    print("Error:", r.status_code)
