# -*- coding: utf-8 -*-
import scrapy
import w3lib.html

class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):

        # /html/body/div/pre/span[1]
        # /html/body/div/pre/span[1]
        # title
        # /html/body/div/pre/span[5]
        #/html/body/div/pre/span[5]
        #/html/body/div/pre/span[5]
        #/html[1]/body[1]/div[1]/pre[1]/span[4]
        # email: /html[1]/body[1]/div[1]/pre[1]/span[8]
        # email /html/body/div/pre/span[8]
        return {
            'email': response.xpath('/html[1]/body[1]/div[1]/pre[1]/span[8]').get(),
            'emailagain from chrome:': response.xpath('/html/body/div/pre/span[8]').get(),
            'titleforme': response.xpath('/html[1]/body[1]/div[1]/pre[1]/span[4]/text()').get(),
            'number': response.xpath('//span[@class="rfc-no"]/text()').get(),
            'title': response.xpath('//meta[@name="DC.Title"]/@content').get(),
            # 'title': response.xpath('//span[@class="title"]/text()').get(),
            'date': response.xpath('//span[@class="date"]/text()').get(),
            # 'date': response.xpath('//meta[@name="DC.Date.Issued"]/@content').get(),
            'description': response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
            'author': response.xpath('//meta[@name="DC.Creator"]/@content').get(),
            # 'author': response.xpath('//span[@class="author-name"]/text()').get(),
            'company': response.xpath('//span[@class="author-company"]/text()').get(),
            'address': response.xpath('//span[@class="address"]/text()').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get()),
            'headings': response.xpath('//span[@class="subheading"]/text()').getall()
        }
