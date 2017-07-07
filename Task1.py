from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://slashdot.org/"

# opening up the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# Grabs each product
containers = page_soup.findAll("article", {"class": "fhitem fhitem-story article usermode thumbs grid_24"})

##Get the name of the link, which is the headline
# container.header.h2.span.a.text

# filename = "product.csv"
# f = open(filename, "w")

# headers = "band, product_name, shipping\n"

# f.write(header)

print("[")
for container in containers:
    print("{")
    headline = container.header.h2.span.a.text

    # author_container = container.findAll("a", {"href":"https://twitter.com/BeauHD"})
    # author = author_container[0].text

    # date_container = container.findAll("time", {"datetime":"on Thursday July 06, 2017 @06:00AM"})
    # datee = date_container[0].text
    # dyt = datetime.datetime(date_container, "%Y-%m-%dT%H:%M:%S+00:00")

    print("Headline: " + headline)
    print("Author: " + "author")
    print("Date: " + "Put timestamp here")
    print("},")
print("]")
