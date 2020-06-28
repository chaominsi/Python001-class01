# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline:
    def process_item(self, item, spider):
        # return item
        movie_title = item['movie_title']
        movie_type = item['movie_type']
        movie_time = item['movie_time']

        output = f'{movie_title},{movie_type},{movie_time}'
        with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as f:
            f.write(output)

        return item
