from bs4 import BeautifulSoup

with open("index.html", encoding='utf-8') as f:
	html_text=f.read()

bs=BeautifulSoup(html_text, 'lxml')


