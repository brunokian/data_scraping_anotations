from parsel import Selector
import requests

URL_BASE = "http://books.toscrape.com/catalogue/"

# baixa o conteudo da página principal
response = requests.get(URL_BASE + "page-1.html")
selector = Selector(text=response.text)

# acessamos o href do h3 para irmos a pagina especifica do livro
href = selector.css(".product_pod h3 a::attr(href)").get()
detail_page_url = URL_BASE + href


# baixa o conteúdo da pagina especifica do livro
detail_response = requests.get(detail_page_url)
detail_selector = Selector(text=detail_response.text)

# recupera a descrição do produto
# ~ significa a tag irmã
description = detail_selector.css("#product_description ~ p::text").get()

print(description)

