# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonMobileDetailsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mobile_name = scrapy.Field()
    mobile_review = scrapy.Field()
    mobile_price = scrapy.Field()
    mobile_imagelink = scrapy.Field()
    pass
