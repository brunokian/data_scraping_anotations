# data_scraping_anotations

# Finalidade

    Trata-se de um repositório para anotações e códigos referentes à "raspagem de dados" (data scraping)

    Usaremos o site "toscrape para realizar as requisições"
    - http://quotes.toscrape.com/


# Anotações

    A raspagem de dados pode ser dividida em dois passos:
        - request a uma rota
        - parse dos dados
    
    Bibliotecas:
        - selenium
        - beautiful soup
        - scrapy
        - requests
        - parsel

python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r requirements.txt

para executar as funções
    - python3 -i <nomeDoArquivo>


parsel
    Para descobrir o selector do elemento que deseja: botão direito no elemento desejado, copy/copy selector

    selec.css(<selector>)

        - neste caso, será retornado um objeto. Para especificar o conteudo do elemento
    
    selec.css(<selector> :: text.get())

    caso queira o href

    selec.css(<selector> :: attr(href).get())

    caso queira o style

    selec.css(<selector> :: attr(style).get())