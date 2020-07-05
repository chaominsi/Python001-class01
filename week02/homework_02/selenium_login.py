from selenium import webdriver


home_url = 'https://shimo.im/login?from=home'

user = '123123@q.com'
pwd = '123456'


dv = webdriver.Chrome()

dv.get(home_url)
dv.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys(user)
dv.find_element_by_xpath('//input[@name="password"]').send_keys(pwd)
dv.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()




