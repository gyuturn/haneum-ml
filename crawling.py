#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

f = open("lolname.txt", 'w')

for page in range(10):
	with urlopen(f'https://www.op.gg/leaderboards/level?region=kr&page={page}') as response:
		soup = BeautifulSoup(response, 'html.parser')
		for anchor in soup.select('strong.summoner-name'):
			data = anchor.get_text()+"\n"
			f.write(data)
f.close()
        

# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))
