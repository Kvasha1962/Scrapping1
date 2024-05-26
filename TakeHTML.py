import bs4
import requests
from bs4 import BeautifulSoup

url:str = "https://dr-shiyan.ru/glikemisheskiy_index.html"

headers:dict[str,str] = {
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36"
			}

response:requests.models.Response = requests.get(url, headers=headers)

bs:bs4.BeautifulSoup=BeautifulSoup(response.content, 'html.parser')

text = str(bs)

with open('index.html', 'w', encoding='utf-8') as f:
	f.write(text)

