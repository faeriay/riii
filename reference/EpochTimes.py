#!/usr/bin/env python
#coding=gbk
__author__ = 'BigData'

import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.epochtimes.com/b5/ncid277_2.htm')
res_text = res.text.decode('utf-8')
print res_text
#soup = BeautifulSoup(res_text)
#for ele in soup.select('.arttitle'):
    #print ele.select('a')[0]['href']