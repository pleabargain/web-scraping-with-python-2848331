# -*- coding: utf-8 -*-


import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return {'title': response.xpath('//span[@class="title"]/text()').get()}


# to run this bad boy
# scrapy runspider ietf.py -o ietf.json