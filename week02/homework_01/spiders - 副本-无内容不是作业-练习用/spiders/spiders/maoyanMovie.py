# -*- coding: utf-8 -*-
import scrapy


class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanMovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
