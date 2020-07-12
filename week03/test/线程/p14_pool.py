import requests
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.baidu.com',
    'http://www.qq.com',
    'http://www.sina.com',
    'http://www.163.com',
    'http://www.taobao.com'
]

pool = ThreadPool(4)

result = pool.map(requests.get, urls)

pool.close()
pool.join()

for i in result:
    print(i.url, i.status_code) 