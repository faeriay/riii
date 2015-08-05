# -*- coding: utf-8 -*-
__author__ = 'jokan'
import requests
from bs4 import BeautifulSoup

res = requests.get()
res_text = res.text.encode('utf8')
#print res_text
soup = BeautifulSoup(res_text)
soup.select('#print_area td')[10].text.encode('utf8')


rec ='http://web.pcc.gov.tw/tps/tpam/main/tps/tpam/tpam_tender_detail.do?searchMode=common&scope=F&primaryKey=51630962'

filename = "%s_%s" %(pkAtmMain, caseno)