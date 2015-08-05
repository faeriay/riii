__author__ = 'jokan'

import requests
from bs4 import BeautifulSoup
for pg in range (0,2):
    res = requests.get('http://news.ltn.com.tw/list/BreakingNews?page={}'.format(pg))
    soup  = BeautifulSoup(res.text)
    for ele in soup.select('.lipic'):
        print ele.select('.picword')[0].text, ele.select('span')[0].text, dic.get(li.select('a')[0].get('class')[0])
