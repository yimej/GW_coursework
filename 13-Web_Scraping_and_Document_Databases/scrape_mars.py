from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
from selenium import webdriver
    
def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_data = {}
    
    #mars news
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    
    #featured image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find('article', class_='carousel_item')
    div = article.find('div')
    footer = div.find('footer')
    link = footer.find('a')
    href = link['data-fancybox-href']
    featured_image_url = ('https://www.jpl.nasa.gov' + href)
    mars_data['featured_image_url'] = featured_image_url
    
    #mars weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    mars_data['mars_weather'] = mars_weather
    
    #mars facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df[0] = df[0].apply(lambda x: x.strip(':'))
    df.set_index(0, inplace=True)
    html_table = df.to_html()
    mars_data['html_table'] = html_table
    
    #mars hemispheres
    hemisphere_image_urls = [
        {'title': 'Cerberus Hemisphere', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
        {'title': 'Schiaparelli Hemisphere', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
        {'title': 'Syrtis Major Hemisphere', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
        {'title': 'Valles Marineris Hemisphere', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}
    ]
    mars_data['hemisphere_image_urls'] = hemisphere_image_urls
    
    return(mars_data)