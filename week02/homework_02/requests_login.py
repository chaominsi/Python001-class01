import requests
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)


# post 测试
# url = 'http://httpbin.org/post'
# r = requests.post(url, data={'user':123456})
# r.json()
# r.status_code
# r.content
# r.text

# s = requests.Session()
# 会话上下文管理器 with
# with requests.Session() as s:
#     s.get(url)

print(ua.random)

# requests石墨登录
header = {
    'User-Agent' : ua.random,
    'Referer' : 'https://shimo.im/login?from=home'
}

data = {
    'email':'1234567@qq.com',
    'mobile': '+86undefined',
    'password':'123456'
}
s = requests.Session()
post_url = 'https://shimo.im/lizard-api/auth/password/login'
home_url = 'https://shimo.im/login?from=home'
r1 = s.get(home_url, headers=header)
r1.text

r = s.post(post_url, data=data, headers=header, cookies=s.cookies)
r.status_code
r.text



