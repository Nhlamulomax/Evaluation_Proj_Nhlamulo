"""Author: Nhlamulo Mbunda
   GitHub: Nhlamulomax
   Email: nhlamulomax@gmail.com
   Task: slashdot.org scraping
"""
from selenium import webdriver
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import datetime
import this

try:
    #Login code
    br = webdriver.Chrome()
    #get url of the login page
    br.get('https://slashdot.org/login.pl')
    username = br.find_element_by_id('unickname')
    username.send_keys('Nhlamulomax')
    password = br.find_element_by_id('upasswrd')
    password.send_keys('nhlamulo@Slashdot')
    password.submit()
    br.close()
except:
    pass
finally:
    #url for the page
    my_url = "https://slashdot.org/"

    # opening up the connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # Grabs each news
    containers = page_soup.findAll("article", {"class": "fhitem fhitem-story article usermode thumbs grid_24"})

    # Input timestamp
    input_date = input("Enter the date -> [yyyy-mm-dd]:")

    print("")
    print("                                          NEWS HEADLINES:\n                                 ")
    print("[")

    for container in containers:

        print("{")

        #Get the Headline
        headline = container.header.h2.span.a.text

        # Get the Author
        author_container = container.header.div.findAll("span", {"class": "story-byline"})
        # author name in new line
        author_name = author_container[0].text
        # Removes new lines in a string
        author_rem_lines = re.sub(r"\s+", " ", author_name)
        # remove frst 10 chars
        author_frst = author_rem_lines[11:]
        # removes all chars aftr space char
        author = author_frst.split(' ')[0]

        #Get the Date
        def fix_date(my_date):
            #Get the month number from month name
            def monthNum(x):
                return {
                    'january': 1,
                    'february': 2,
                    'march': 3,
                    'april': 4,
                    'may': 5,
                    'june': 6,
                    'july': 7,
                    'august': 8,
                    'september': 9,
                    'october': 10,
                    'november': 11,
                    'december': 12
                }.get(x, None)

            #format my date [yyyy-mm-dd]
            date_format = (my_date[4] + str(monthNum(my_date[2].lower())) + my_date[3]).replace(',', '')
            fixed_date = datetime.datetime.strptime(date_format, "%Y%m%d").date()

            return fixed_date

        #Get the atticle date [yyyy-mm-dd]
        article_date = fix_date(container.parent.find('time').text.split(' ')).strftime('%Y-%m-%d')
        #Get the timestamp, convert date to timestamp
        timeStamp = int(time.mktime(datetime.datetime.strptime(article_date, "%Y-%m-%d").timetuple()))

        if input_date < article_date:
            print("  Headline: " + headline)
            print("  Author: " + author)
            #print("  Date: " + article_date)
            print("  Date: " + str(timeStamp))
        else:
            print("Nothing to be displayed, SORRY!!!")

        print("},")
    print("]")
