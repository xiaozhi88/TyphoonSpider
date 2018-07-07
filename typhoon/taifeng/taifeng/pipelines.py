# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

from taifeng.items import TaifengItem


class TaifengPipeline(object):

    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONGODB_HOST'],
                                   port=settings['MONGODB_PORT'])
        self.db = conn[settings['MONGODB_DB']]
        self.collection = self.db[TaifengItem.collections]

    def process_item(self, item, spider):
        self.collection.update({'name': item['name']}, {'$set': item}, True)
        return item
