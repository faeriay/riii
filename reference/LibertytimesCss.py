__author__ = 'jokan'

import requests
import re
res = requests.get('http://news.ltn.com.tw/css/news/style.css?20150715')
res.encoding = 'utf-8'
print res.text
dic ={}
tabs =re.findall('.list span a.(tab\d+):after{content:"(.*?).*?"}', res.text)
for tab in tabs:
    print dic[tab[0]],tab[1]