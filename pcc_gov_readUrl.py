__author__ = 'jokan'

import requests
from bs4 import BeautifulSoup

def caseno(rec):
    res = requests.get(rec)
    res_text = res.text.encode('utf8')
    #print res_text
    soup = BeautifulSoup(res_text)
    return soup.select('#print_area td')[10].text.encode('utf8')

f = open("bid_url.txt","r")
for line in f.readlines():
    rec = line.strip()
    #print rec
    pkAtmMain = rec.split('primaryKey=')[1]
    res_get = requests.get(rec)
    res_text = res_get.text.encode('utf8')
    son_soup = BeautifulSoup(res_text)
    printarea = son_soup.select('#print_area')[0]
    bidfile = open("data/%s_%s.txt"%(pkAtmMain,caseno(rec)),"w")
    bidfile.write(printarea.prettify('utf8'))
    bidfile.close()
f.close()