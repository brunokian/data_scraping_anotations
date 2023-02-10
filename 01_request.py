import requests

# Requisição get
response = requests.get("http://books.toscrape.com/")

print(response.status_code)
print(response.headers)
print(response.headers["Content-Type"])
print(response.text) # conteudo html cru
print(response.content) # conteudo binário
print(response.json())
response.raise_for_status()

# Requisição do tipo post
responsePost = requests.post("http://httpbin.org/post", data="some content")
print(response.text)

# Requisição enviando cabeçalho (header)
responseHeaders = requests.get("http://httpbin.org/get", headers={"Accept": "application/json"})
print(responseHeaders.text)