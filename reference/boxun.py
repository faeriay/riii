# -*- coding: utf-8 -*-
__author__ = 'BigData'
import requests
from bs4 import BeautifulSoup
rs = requests.session()
res = rs.get('http://www.boxun.com/search.shtml')
year='2014'
month='10'
dataform = {'cat':'china','year':year,'month':month,'date':'all'}

header ={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'37',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'__gads=ID=f2d671063f7ad81d:T=1438725394:S=ALNI_MYRLgnV6pI_AV0XmQYGW_JBP5dVgA; __utma=204650115.1892445826.1438725394.1438725394.1438736681.2; __utmc=204650115; __utmz=204650115.1438736681.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.2.1892445826.1438725394',
    'Host':'boxun.com',
    'Origin':'http://boxun.com',
    'Referer':'http://boxun.com/search.shtml',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
}

res = requests.post('http://www.boxun.com/cgi-bin/search/find_by_date.cgi', data=dataform, headers=header)

res_text = res.text.encode('utf-8')
soup = BeautifulSoup(res_text)
#for ele in soup.select('li'):
#   link = ele.select('a')[0]['href']


link = soup.select('li a')[0]['href']
joinlink='http://boxun.com'+link
pg_rs =requests.get(joinlink)
pg_text = pg_rs.text.encode('utf-8')
pg_soup = BeautifulSoup(pg_text)
print pg_soup.select('table')[3]('center')[0].text.encode('utf-8')






