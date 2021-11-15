#!/usr/bin/env python
# coding: utf-8

# In[232]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[233]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[234]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[235]:


# get the most recent news article and summary
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[236]:


slide_elem.find('div', class_='content_title')


# In[237]:


# extract the text from the other junk
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[238]:


#get the teaser
news_summary = slide_elem.find('div', class_='article_teaser_body').get_text()
news_summary


# In[239]:


#get the image
#news_image = slide_elem.find('img').get('src')
#news_image


# ### Featured Images

# In[240]:


#images
# visit url
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[241]:


# find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[242]:


# parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[243]:


# grab the image data
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[244]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
print(img_url)


# In[245]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[246]:


df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# Hemispheres

# In[263]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

jpg_soup = soup(html, 'html.parser')


# In[264]:


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


# In[265]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[266]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:


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

