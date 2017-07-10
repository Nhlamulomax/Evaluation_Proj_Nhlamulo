#Import packages
from asyncore import read
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#connect and read the site with url provided
my_url = "http://www.imdb.com/find?q=Movies&s=tt&ttype=ft&ref_=fn_ft"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parsing html
page_soup = soup(page_html, "html.parser")

#Grabs all movie's title
containers = page_soup.findAll("td", {"class":"result_text"})
tit = containers[0]
title = tit.text
print(title)
#input search string
search_string = input("Enter a searsch string: ")
#SearchMe = "The apple is red and the berry is blue!"
#print(SearchMe.find("is"))
print(title.find(search_string))
num = title.find(search_string)  #number of searched string
if num > 0:
    # loop for frst 10 titles
    i = 0
    while i <= 9:
        # print the Title and date of each tittle
        print("Title: " + title)
        print("Date: " + "Date here")
        print("")
        i = i + 1