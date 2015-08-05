
    # -*- coding: utf-8 -*-
__author__ = 'jokan'

import requests
from bs4 import BeautifulSoup

payload ={
    'method':'search',
    'searchMethod':'true',
    'tenderUpdate':'',
    'searchTarget':'',
    'orgName':'',
    'orgId':'',
    'hid_1':'1',
    'tenderName':'',
    'tenderId':'',
    'tenderWay':'1',
    'tenderDateRadio':'on',
    'tenderStartDateStr':'104/07/24',
    'tenderEndDateStr':'104/07/30',
    'tenderStartDate':'104/07/24',
    'tenderEndDate':'104/07/30',
    'isSpdt':'N',
    'proctrgCate':'3',
    'radProctrgCate':'3',
    'btnQuery':'查詢',
    'hadUpdated':''
}
rs = requests.session()
user_post = rs.post("http://web.pcc.gov.tw/tps/pss/tender.do?\
searchMode=common&searchType=basic", data=payload)
res_post = user_post.text.encode('utf8')

pg_format = "http://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=basic&method=search&isSpdt=&pageIndex={}"

f = open('bid_url.txt','w')
for pg in range(1,4):
    user_get = rs.get(pg_format.format(pg))
    #print user_get
    res = user_get.text.encode('utf8')
    soup = BeautifulSoup(res)
    soup_table = soup.select('#print_area')[0]
    soup_rows = soup_table.select('tr')[1:-1]
    #print soup_rows[0].encode('utf8')
    for soup_row in soup_rows:
        link_href = soup_row.select('a')[0]['href'][3:]
        son_pg = 'http://web.pcc.gov.tw/tps/'+link_href
        detail = son_pg+'\n'
        f.write(detail)
f.close()