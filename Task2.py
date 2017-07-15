"""Author: Nhlamulo Mabunda
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

#Function for daate
def date():
    contain_date = page_soup.findAll("h4")
    date_text = contain_date[0].text
    trim_date = date_text.lstrip('Weekend of ')
    yr = trim_date.split(',', 1)[1]
    day_mon = trim_date.split('-')[0]
    date = yr + ',' + day_mon
    return date

#Function for searching
def search(movies_lst, str_search):
    match_lst = []
    for i in range(len(movies_lst)):
        title = movies_lst[i].text
        if title.find(str_search) != -1:
            #'Hello world'.replace('world', 'Guido')
           match_lst.append(title.replace('\n', ' ') + " -> " + date())
    return print(match_lst)

#list of all the movies
movies_lst = page_soup.findAll("td", {'class': ['titleColumn']})

#input search string
str_search = input ("Enter the search string: ")

#calling of my search function passing movies_lst and str_search
search(movies_lst,str_search)
