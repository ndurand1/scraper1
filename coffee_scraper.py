#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:08:51 2020

@author: npdur
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

main_url = "https://www.coffeebeancorral.com/categories/Green-Coffee-Beans/All-Coffees.aspx"

# request page
request_page = urlopen(main_url)
page_html = request_page.read()
request_page.close()

html_soup = bs(page_html, 'html.parser')

coffee_data = html_soup.find_all('div', class_="product-info")

# create csv with coffee names and prices
filename = 'green_coffee_prices.csv'
f = open(filename, 'w')

headers = 'Coffee, Price \n'

f.write(headers)

# loop through page data using divs
for coffee in coffee_data:
	bean = coffee.find('div', class_="SingleProductDisplayName recordname").text
	price = coffee.find('div', class_="SingleProductDisplayPrice recordprice").text
	
	# for some reason this has both leading and following newlines on bean and price
	f.write(bean + ',' + price)

f.close()

print("Success! Check for file in current working directory.")	