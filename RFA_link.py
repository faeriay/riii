# -*- coding: utf-8 -*-
__author__ = 'jokan'
import requests
from bs4 import BeautifulSoup
year = 2015
month = '07'
link = 'http://www.rfa.org/mandarin/yataibaodao\
/story_archive?year=%d&b_start:int={}&month=%s'%(year,month)
f = open('rfa_link.txt','w')
for pg in range(0,31,30):
    res = requests.get(link.format(pg))
    res_text = res.text.encode('utf-8')
    soup = BeautifulSoup(res_text)
    for ele in soup.select('.sectionteaser'):
        if len(ele.select('h2 a')) > 0:
            link = ele.select('h2 a')[0]['href'].encode('utf-8')+'\n'
            f.write(link)
        else:
            print 'error'
f.close()