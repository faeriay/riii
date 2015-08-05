# -*- coding: utf-8 -*-
__author__ = 'jokan'
import requests
from bs4 import BeautifulSoup
year = 2015
month = '06'
link_q = 'http://www.rfa.org/mandarin/yataibaodao\
/story_archive?year=%d&b_start:int={}&month=%s'%(year,month)

for pg in range(0,390,30):
    res = requests.get(link_q.format(pg))
    res_text = res.text.encode('utf-8')
    soup = BeautifulSoup(res_text)
    for ele in soup.select('.sectionteaser'):
        if len(ele.select('h2 a')) > 0:
            link = ele.select('h2 a')[0]['href']
            page = requests.get(link)
            page_text = page.text.encode('utf-8')
            soup = BeautifulSoup(page_text)
            header = soup.select('#storypagemaincol h1')[0].text.encode('utf-8')
            date_temp = soup.select('#story_date')[0].text.encode('utf-8')
            date =date_temp.replace('-','')
            title = date+' '+header
            f = open('data/%s.txt'%(title),'w')
            f.write(title+'\n'+'\n'+'[RFA]'+'\n'+'\n')
            for ele in range(0,len(soup.select('#storytext p'))) :
                content = soup.select('#storytext p')[ele].text.encode('utf-8')
                f.write(content+'\n'+'\n')
            f.close()