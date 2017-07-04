import requests
from bs4 import BeautifulSoup

r = requests.get("https://slashdot.org")
#r.content
soup = BeautifulSoup(r.content)

print soup.prettify()
