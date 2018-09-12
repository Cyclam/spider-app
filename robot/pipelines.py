# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class DoubanImgPipeline(object):
    def process_item(self, item, spider):
        return item

class DoubanImgDownloadPipeline(ImagesPipeline):
    default_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'bid=OKGyc--96Yk; gr_user_id=81858c84-e067-4c09-85f7-7cdb95af704b; __utmc=30149280; _vwo_uuid_v2=D293A29620DAB8FDF6F7067CB264EEFE9|620b80437646d306e8f631eebc42957a; viewed="1929984_2179813"; ll="118282"; dbcl2="71583332:3xY+TJGGjGY"; _ga=GA1.2.999125332.1531119417; ck=ORtd; push_doumail_num=0; __utmv=30149280.7158; push_noty_num=0; __utmz=30149280.1536721268.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; __utmz=223695111.1536721268.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __yadk_uid=iJW8LdoV8J6MabAuy5piYCNREgI2TBOd; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1536732716%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.999125332.1531119417.1536721268.1536732716.4; __utmb=30149280.0.10.1536732716; __utma=223695111.999125332.1531119417.1536721268.1536732716.2; __utmb=223695111.0.10.1536732716; ct=y; _pk_id.100001.4cf6=2f288a13064822e7.1536721268.2.1536735584.1536722472.',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    def get_media_requests(self, item, info):
        for url in item['image_urls']:
            print('========================================================')
            print(url)
            print('========================================================')
            self.default_headers['referer'] = url[0]
            yield Request(url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_urls'] = image_paths
        return item