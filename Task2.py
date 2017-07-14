"""Author: Nhlamulo Mbunda
   GitHub: Nhlamulomax
   Email: nhlamulomax@gmail.com
   Task: www.imdb.com scraping
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import this

#url of the page
my_url = "http://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht_2"

# opening up the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#Function for searching process
def search(movies_lst, str_search):
    match_lst = []
    for i in range(len(movies_lst)):
        title = movies_lst[i].text
        if title.find(str_search) != -1:
           match_lst.append(title)
    return print(match_lst)

#list of all the movies
movies_lst = page_soup.findAll("td", {'class': ['titleColumn']})
#input search string
str_search = input ("Enter the search string: ")

#calling of my search function passing movies_lst and str_search
search(movies_lst,str_search)


