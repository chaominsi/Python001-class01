# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

dbInfo = {
    'host' : "localhost",
    'port' : 3306,
    'user' : 'root',
    'password' : 'root',
    'db' : 'geek_pro'
}

sqls = ['select 1', 'select VERSION()']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db,
        )
        
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())

                cur.close()
                conn.commit()
        except:
            conn.rollback()

        conn.close()



class SpidersPipeline:
    def process_item(self, item, spider):
        movie_title = item['movie_title']
        movie_type = item['movie_type']
        movie_time = item['movie_time']

        # 之前是存入文件，将其改写为存入数据库
        db = ConnDB(dbInfo, sqls)
        db.run()
        print(result)


        return item





