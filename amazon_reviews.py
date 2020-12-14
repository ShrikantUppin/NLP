# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:04:42 2020

@author: SHRIKANT
"""

# Step1: Import required libraries...

from bs4 import BeautifulSoup as bs
import requests


# Step 2: Provide Link from where you want to scrap data..

link = 'https://www.amazon.in/boAt-BassHeads-100-Headphones-Black/product-reviews/B071Z8M4KX/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page = requests.get(link)

# print(page) it will show output as 200

soup = bs(page.content, 'html.parser')
soup.prettify()

user_names = soup.find_all('span', class_='a-profile-name')
print(user_names)