# -*- coding: utf-8 -*-

# 带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代，工作原理同上。
# yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
# 简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。

# Scrapy首先读取定义在 start_urls 属性中的URL，创建请求，并且将接收到的response作为参数调用默认的回调函数 parse，来启动爬取。

from scrapy import Request
from scrapy.spiders import Spider
from robot.items import DoubanMoveItem                                                                                                                                                                                                                                                                                                                                                                           

class DoubanSpider(Spider):
    name = 'douban'
    headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' }
    allowed_domains = ['douban.com']
    start_urls = 'https://movie.douban.com/top250'

    # 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
    # 当spider启动爬取并且未制定URL时，该方法被调用。 当指定了URL时，make_requests_from_url() 将被调用来创建Request对象。 该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器。
    # 该方法的默认实现是使用 start_urls 的url生成Request。
    def start_requests(self):
        url = self.start_urls
        yield Request(url, headers=self.headers)

    # 该方法及其他的Request回调函数必须返回一个包含 Request、dict 或 Item 的可迭代的对象。
    def parse(self, response):
        item = DoubanMoveItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            # 要实际提取文本数据，必须调用选择器.extract()方法
            item['rank'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            yield item

        # next_url = response.xpath('//span[@class="next"]/a/@href').extract() # <class 'list'>
        # if next_url:
        #     next_url = self.start_urls + next_url[0]
        #     yield Request(next_url, headers=self.headers)