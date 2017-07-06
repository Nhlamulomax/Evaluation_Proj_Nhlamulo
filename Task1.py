from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://slashdot.org/"

#opening up the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#Grabs each field
containers = page_soup.findAll("article",{"class":"fhitem fhitem-story article usermode thumbs grid_24"})

##Get the name of the link, which is the headline
#container.header.h2.span.a.text

#Also using CSV file to display my news headlines
#filename = "product.csv"
#f = open(filename, "w")

#headers = "Task 1: News headlines\n"

#f.write(headers)

for container in containers:

	headline = container.header.h2.span.a.text

	author_container = container.findAll("a", {"href":"https://twitter.com/BeauHD"})
	author = author_container[0].text

	#date_container = container.findAll("time", {"datetime":"on Thursday July 06, 2017 @06:00AM"})
	#datee = date_container[0].text

	print("Headline: " + headline)
	print("Author name: " + author)
	#print("Date: " + datee)

#datee = 10

	#f.write(headline + "," + author + "," + datee + "\n")
#f.close()


