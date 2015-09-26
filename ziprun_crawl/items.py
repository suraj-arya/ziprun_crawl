# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZiprunCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    restuarant_name = scrapy.Field()
    phone = scrapy.Field()
    delivery = scrapy.Field()
    reviews = scrapy.Field()
    checkin = scrapy.Field()
    rating = scrapy.Field()
    cuisines = scrapy.Field()
    establishment = scrapy.Field()
    address = scrapy.Field()
    bookmarks = scrapy.Field()