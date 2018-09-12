# -*- coding: utf-8 -*-

from scrapy import Request
from scrapy.spiders import Spider
from robot.items import DoubanImageItem 


class ZhihuSpider(Spider):
    name = 'zhihu'
    headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' }
    allowed_domains = ['douban.com']
    start_urls = 'https://movie.douban.com/top250'

    def start_requests(self):
        url = self.start_urls
        yield Request(url, headers=self.headers)

    # 该方法及其他的Request回调函数必须返回一个包含 Request、dict 或 Item 的可迭代的对象。
    def parse(self, response):
        item = DoubanImageItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            # 要实际提取文本数据，必须调用选择器.extract()方法
            item['image_urls'] = movie.xpath('.//div[@class="pic"]/a/img/@src').extract()
            print(item['image_urls'])
            yield item
