# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class ArticleCrawlerPipeline:
#     def process_item(self, item, spider):
#         return item

#import exceptions from scrapy
from scrapy.exceptions import DropItem
#import datetime object
from datetime import datetime


class CheckItemPipeline:
    def process_item(self, article, spider):
        if not article['lastUpdated'] or not article['title'] or not article['url']:
            raise DropItem("Missing data!")
        #return the article
        return article

#create class for cleaning the date
class CleanDatePipeline:
    def process_item(self, article, spider):
        #convert the date to a datetime object
        article['lastUpdated'].replace('This page was last edited on', '').strip()
        article['lastUpdated']= datetime.strftime(article['lastUpdated'], '%d %B %Y, at %H:%M')
        
        #return the article
        return article
