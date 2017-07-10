from selenium import webdriver
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import datetime
from time import strptime
from datetime import date
import requests
from lxml import html
import this

try:
    br = webdriver.Chrome()
    br.get('https://slashdot.org/login.pl')
    username = br.find_element_by_id('unickname')
    username.send_keys('Nhlamulomax')
    password = br.find_element_by_id('upasswrd')
    password.send_keys('nhlamulo@Slashdot')
    password.submit()
except:
    print("")
finally:
    # Scraping code
    my_url = "https://slashdot.org/"

    # opening up the connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # Grabs each product
    containers = page_soup.findAll("article", {"class": "fhitem fhitem-story article usermode thumbs grid_24"})

    # Input timestamp
    input_tymstamp = input("                                              Enter the timestamp: ")

    print("")
    print("                                          NEWS HEADLINES:\n                                 ")
    print("[")

    for container in containers:

        print("{")

        # Headline
        headline = container.header.h2.span.a.text

        # Author
        author_container = container.header.div.findAll("span", {"class": "story-byline"})
        # author name in new line
        author_name = author_container[0].text
        # Removes new lines in a string
        author_rem_lines = re.sub(r"\s+", " ", author_name)
        # remove frst 10 chars
        author_frst = author_rem_lines[11:]
        # removes all chars aftr space char
        author = author_frst.split(' ')[0]

        # Timestamp
        date_container = container.header.div.findAll("span", {"class": "story-byline"})
        # author name in new line
        date_name = date_container[0].text
        # Removes new lines in a string
        date_rem_lines = re.sub(r"\s+", " ", date_name)
        # remove frst 10 chars
        date_frst = date_rem_lines[11:]  # msmash on Friday July 07, 2017 @09:47PM from the tussle-continues dept.
        # Remove author name
        rem_author = date_frst.lstrip(author)  # on Friday July 07, 2017 @09:47PM from the tussle-continues dept.
        # Remove 'on ' in date_date
        rem_ON = rem_author.lstrip('on ')  # Friday July 07, 2017 @09:47PM from the tussle-continues dept.
        # Remove everything and liv the date
        date_date = rem_ON.split(' from')[0]  # Friday July 07, 2017 @09:47PM
        # Day
        my_day = date_date.split(' ')[0]  # Friday
        # remove day
        date_time = date_date.lstrip(my_day)
        # Trim date_time
        trim_date_time = date_time.strip()  # July 07, 2017 @05:21PM
        # my_month
        my_month = trim_date_time.split(' ')[0]  # July
        # Remove month
        rem_month = trim_date_time.lstrip(my_month)
        # Trim
        trim_rem_month = rem_month.strip()
        # my_daynum
        my_daycom = trim_rem_month.split(' ')[0]  # 07,
        my_daynum = my_daycom.split(',')[0]  # 07
        # Remove month and day
        rem_month_day = trim_date_time.lstrip(my_month + " " + my_daycom)  # 2017 @05:21PM
        my_year = (rem_month_day.split(' ')[0]).strip()
        # Month format
        month_format = my_month[:3]
        # Change month name to month num
        month_name = month_format
        month_number = str(strptime(month_name, '%b').tm_mon)
        test = datetime.datetime.now().date()  # Today's date
        # TimeStamp
        d8tym = date(int(my_year), int(month_number), int(my_daynum))
        timestamp2 = time.mktime(d8tym.timetuple())
        # Today's timestamp
        tday = date.today()
        tdays_timestamp = time.mktime(tday.timetuple())  # 1499551200.0

        # Output the headlines, author and date of ne
        if float(input_tymstamp) <= float(tdays_timestamp):  # 1499464800.0
            print("  Headline: " + headline)
            print("  Author: " + author)
            print("  Date: " + str(timestamp2))

        print("},")
    print("]")