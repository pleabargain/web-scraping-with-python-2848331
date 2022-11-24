# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


# make sure the objects in the class match the names in the wikipedia.py script!
# otherwise you'll get all kinds of key errors!
import scrapy


# create items for the data we want to scrape
class Article(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    lastUpdated = scrapy.Field()

    
