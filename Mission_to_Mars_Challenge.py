#!/usr/bin/env python
# coding: utf-8


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# get the most recent news article and summary
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')


# extract the text from the other junk
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title




#get the teaser
news_summary = slide_elem.find('div', class_='article_teaser_body').get_text()
news_summary




#get the image
#news_image = slide_elem.find('img').get('src')
#news_image


# ### Featured Images


#images
# visit url
url = 'https://spaceimages-mars.com/'
browser.visit(url)




# find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()




# parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')




# grab the image data
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel




img_url = f'https://spaceimages-mars.com/{img_url_rel}'
print(img_url)




df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df



df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)
jpg_soup = soup(html, 'html.parser')


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# let's grab one and see how that goes -- ok, now let's write a for loop
# I found the find_by_text on https://splinter.readthedocs.io/en/latest/finding.html, also .value
for x in range(0, 4):
    full_image_link = browser.links.find_by_partial_text('Hemisphere')[x]
    full_image_link.click()
    hi_res_link = browser.links.find_by_text('Sample')
    full_img_url = hi_res_link['href']
    img_title = browser.find_by_tag('h2').value
    hemispheres = {img_title : full_img_url}
    hemisphere_image_urls.append(hemispheres)
    browser.visit(url)


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()


# old code
# full_image_link = browser.find_by_tag('h3')[0]

# code for reference

#find button, click to get full image
#full_image_elem = browser.find_by_tag('button')[1]
#full_image_elem.click()

#use soup to parse
#html = browser.html
#img_soup = soup(html, 'html.parser')

#grab short url
#img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
#img_url_rel

#concatenate url to make full url
#img_url = f'https://spaceimages-mars.com/{img_url_rel}'
#print(img_url)

