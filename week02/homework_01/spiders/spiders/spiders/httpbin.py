# -*- coding: utf-8 -*-
import scrapy

# setting增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过 Request.meta['proxy'] 读取http_proxy环境变量加载代理

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    # ip查看请求方ip
    start_urls = ['http://httpbin.org/ip']
    # headers查看user-agent
    # start_urls = ['http://httpbin.org/headers']

    def parse(self, response):
        print(response.text)
