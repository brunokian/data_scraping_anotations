from parsel import Selector
import requests

response = requests.get("http://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
selector = Selector(text=response.text)

# title = selector.css('.default h1 ::text').get()
# print(title)

# titlesOfBooks = selector.css(".product_pod h3").getall()
# print(titlesOfBooks)

# titlesOfBooks = selector.css(".product_pod h3 a::attr(title)").getall()
# print(titlesOfBooks)

# prices = selector.css(".product_price .price_color ::text").getall()
# print(prices)

# next_page_url = selector.css(".next a::attr(href)").get()
# print(next_page_url)