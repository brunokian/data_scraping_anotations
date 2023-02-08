import requests
from requests.exceptions import ConnectTimeout, HTTPError

def fetch_html(base_url):
    try:
        res = requests.get(base_url)
    except (ConnectTimeout, HTTPError):
        return ''

    return res.text
    
def scrape_all_quotes():
    base_url = 'http://quotes.toscrape.com/'
    return fetch_html(base_url)