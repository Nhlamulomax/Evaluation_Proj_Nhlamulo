#Import packages
from asyncore import read
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#connect and read the site with url provided
my_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=Movies&s=tt"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parsing html
page_soup = soup(page_html, "html.parser")

#Grabs each movie's title
containers = page_soup.findAll("td", {"class":"result_text"})

#input search string
search_string = input("Enter a searsch string: ")

#loop for frst 10 titles
i = 0
while i <= 9:

    title = str(containers[i])

    if title == search_string:
        # print the Title and date of each tittle
        print("Title: " + title)
        print("Date: " + "Date here")
        print("")
        i = i + 1








