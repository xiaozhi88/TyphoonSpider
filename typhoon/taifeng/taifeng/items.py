# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaifengItem(scrapy.Item):
    collections = 'taifeng'
    tfbh = scrapy.Field()
    name = scrapy.Field()
    ename = scrapy.Field()
    begin_time = scrapy.Field()
    end_time = scrapy.Field()
    points = scrapy.Field()

