__author__ = 'Asi'

import requests
from bs4 import BeautifulSoup

r = requests.get("http://oreilly.com/store/samplers.html")

c = r.content
soup = BeautifulSoup(c)
samples = soup.find_all("a", "item-title")

count = 0
for i in samples:
    print i