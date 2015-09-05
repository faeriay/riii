# -*- coding: utf-8 -*-
__author__ = 'jokan'
import requests
from bs4 import BeautifulSoup
page = requests.get('http://www.rfa.org/mandarin/yataibaodao/jingmao/cyl-07312015110242.html')
page_text = page.text.encode('utf-8')
soup = BeautifulSoup(page_text)
header = soup.select('#storypagemaincol h1')[0].text.encode('utf-8')
date_temp = soup.select('#story_date')[0].text.encode('utf-8')
date =date_temp.replace('-','')
title = date+' '+header
f = open('%s.txt'%(title),'w')
f.write(title+'\n'+'\n'+'[RFA]'+'\n'+'\n')
for ele in range(0,len(soup.select('#storytext p'))) :
    content = soup.select('#storytext p')[ele].text.encode('utf-8')
    f.write(content+'\n'+'\n')
f.close()