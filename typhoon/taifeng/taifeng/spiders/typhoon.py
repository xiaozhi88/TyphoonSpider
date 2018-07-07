import json

from scrapy import Request
from scrapy.spiders import Spider
from taifeng.items import TaifengItem


class TyphoonSpider(Spider):
    name = 'typhoon'
    start_typhoon_urls = 'http://www.wztf121.com/data/complex/{year}{month}.json?'
    def start_requests(self):
        """
        获取url
        :return: 各月份的url
        """
        for y in range(2000,2019):
            for n in range(1,13):
                m = '%02d'%n
                yield Request(self.start_typhoon_urls.format(year=y,month=m),callback=self.parse_one)

    def parse_one(self, response):
        """
        解析历史台风信息
        :param response: 历史台风信息
        :return: 解析的台风内容
        """
        res = json.loads(response.text)[0]
        item = TaifengItem()
        item["tfbh"] = res["tfbh"]
        item["name"] = res["name"]
        item["ename"] = res["ename"]
        item["begin_time"] = res["begin_time"]
        item["begin_time"] = res["begin_time"]
        item["end_time"] = res["end_time"]
        item["points"] = res["points"]
        yield item

