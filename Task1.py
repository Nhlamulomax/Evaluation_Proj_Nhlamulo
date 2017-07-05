#import requests
#from bs4 import BeautifulSoup

#r = requests.get("https://slashdot.org")
#r.content
#soup = BeautifulSoup(r.content)

#print soup.prettify()
########################################################

import requests
from bs4 import BeautifulSoup

url = "https://slashdot.org"
req = requests.get(url)

soup = BeautifulSoup(req.content)
links = soup.find_all("a")

#Print all the links
#for link in links:
       # print "<a href='%s'>%s</a>" % (link.get("href"), link.text)

#g_headlines = soup.find_all("div", {"class": "infor"})
g_headlines = soup.find_all("a", {"href": "//hardware.slashdot.org/story/17/07/05/023222/call-for-a-ban-on-child-sex-robots"})

for h in g_headlines:
    print h.text