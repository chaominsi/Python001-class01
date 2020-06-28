import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://maoyan.com/films?showType=3'

headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "br, gzip, deflate",
    "Accept-Language": "zh-cn",
    "Host": "httpbin.org",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
  }

response = requests.get(url,headers=headers)
print(response.text)
print(response.status_code)


# content = response.text
with open('.//html_code.txt', 'r', encoding='utf-8') as f:
    content = f.read()


bs_info = bs(content,'html.parser')

tag_list = bs_info.find_all('div',attrs={'class':'movie-item-hover'})
print(len(tag_list))
# 解析数据
movie_list = [['电影名称', '电影类型', '上映时间s']]
for tags in tag_list:
    movie_name = tags.find('span',attrs={'class':'name'}).text
    movie_type = tags.find_all('div',attrs={'class':'movie-hover-title'})[1].text.strip()
    movie_time = tags.find('div',attrs={'class':'movie-hover-title movie-hover-brief'}).text.strip()

    movie = [movie_name, movie_type, movie_time]
    movie_list.append(movie)

    # print(name)
    # print(movie_type)
    # print(movie_time)


# 保存数据
df = pd.DataFrame(data=movie_list)

df.to_csv('./movie1.csv', encoding='utf-8', index=False,header=False)
