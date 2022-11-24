# -*- coding: utf-8 -*-

# to run this script
# the -s option is to set the settings.py file
# scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# import the Article class from items.py
from article_crawler.items import Article

class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Kevin_Bacon']

    rules = [
        Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)
    ]

    def parse_info(self, response): 
        article   = Article()
        
        article[ "title"]= response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()'),
        article[ "url"]= response.url
        article["lastUpdated"]= response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
        
