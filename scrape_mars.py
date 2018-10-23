
# coding: utf-8

from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


url = ('https://mars.nasa.gov/news/')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# # Scraping


#print(soup.prettify())


# # NASA Mars News


# pull titles from website
titles = soup.find_all('div', class_="content_title")
print(titles)


# pull body from website
body = soup.find_all('div', class_="rollover_description")
#print(body)


# pull titles and body from website
results = soup.find_all('div', class_="slide")
for result in results:
    titles = result.find('div', class_="content_title")
    title = titles.find('a').text
    bodies = result.find('div', class_="rollover_description")
    body = bodies.find('div', class_="rollover_description_inner").text
    print('----------------')
    print(title)
    print(body)
    


# # JPL Mars Space Images - Featured Image


url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


#print(soup.prettify())


# pull images from website
images = soup.find_all('a', class_="fancybox")
#print(images)


# pull image link
pic_src = []
for image in images:
    pic = image['data-fancybox-href']
    pic_src.append(pic)

featured_image_url = 'https://www.jpl.nasa.gov' + pic
featured_image_url
    


# # Mars Weather

url = ('https://twitter.com/marswxreport?lang=en')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


#print(soup.prettify())


contents = soup.find_all("div",class_="content")
#print(content)


weather_mars = []
for content in contents:
    tweet = content.find("div", class_="js-tweet-text-container").text
    weather_mars.append(tweet)
#print(weather_mars)

mars_weather = weather_mars[8]
print(mars_weather)


# # Mars Facts


mars_facts_url = "https://space-facts.com/mars/"
table = pd.read_html(mars_facts_url)
table[0]

df = table[0]
df.columns = ["Facts", "Value"]
df.set_index(["Facts"])
df


facts_html = df.to_html()
facts_html = facts_html.replace("\n","")
facts_html


# # Mars Hemispheres

hemisphere_image_urls = []


# Cerberus Hemispheres


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# print(soup.prettify())


cerberus_img = soup.find_all('div', class_="wide-image-wrapper")
print(cerberus_img)


for img in cerberus_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
cerberus_title = soup.find('h2', class_='title').text
print(cerberus_title)
cerberus_hem = {"Title": cerberus_title, "url": full_img}
print(cerberus_hem)


# Schiaparelli Hemisphere


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


#print(soup.prettify())


shiaparelli_img = soup.find_all('div', class_="wide-image-wrapper")
print(shiaparelli_img)



for img in shiaparelli_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
shiaparelli_title = soup.find('h2', class_='title').text
print(shiaparelli_title)
shiaparelli_hem = {"Title": shiaparelli_title, "url": full_img}
print(shiaparelli_hem)


# Syrtis Hemisphere


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


#print(soup.prettify())


syrtris_img = soup.find_all('div', class_="wide-image-wrapper")
print(syrtris_img)


for img in syrtris_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
syrtris_title = soup.find('h2', class_='title').text
print(syrtris_title)
syrtris_hem = {"Title": syrtris_title, "url": full_img}
print(syrtris_hem)


# Valles Marineris Hemisphere



url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


valles_marineris_img = soup.find_all('div', class_="wide-image-wrapper")
print(valles_marineris_img)



for img in valles_marineris_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
valles_marineris_title = soup.find('h2', class_='title').text
print(valles_marineris_title)
valles_marineris_hem = {"Title": valles_marineris_title, "url": full_img}
print(valles_marineris_hem)

