# -*- coding: utf-8 -*-
import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        for i in range(10):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-item-hover"]/a')
        items = []
        for movie in movies:
            movie_title = movie.xpath('./div/div/span[@class="name "]/text()')
            movie_type = movie.xpath('./div/div[2]/text()')
            movie_time = movie.xpath('./div/div[4]/text()')

            item = SpidersItem()

            item['movie_title'] = movie_title
            item['movie_type'] = movie_type
            item['movie_time'] = movie_time
            
        return items


