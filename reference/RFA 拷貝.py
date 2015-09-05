# -*- coding: utf-8 -*-
__author__ = 'BigData'
import requests
from bs4 import BeautifulSoup
link = 'http://www.rfa.org/mandarin/yataibaodao/story_archive?year=2015&b_start:int={}&month=06'
#pg =600

for pg in range(0,61,30):
    res = requests.get(link.format(pg))
    res_text = res.text.encode('utf-8')
    soup = BeautifulSoup(res_text)
    for ele in soup.select('.sectionteaser'):
        if len(ele.select('h2 a')) > 0:
            print ele.select('h2 a')[0].text
        else:
            print 'error'