# -*- coding:utf-8 -*-
import os
import requests
import re
from bs4 import BeautifulSoup

from lxml.html.defs import font_style_tags

def spider():
    url = "http://www.airenti55.net/"
    #proxies = {"http": "http://172.17.18.80:8080", "https": "https://172.17.18.80:8080"}
    #r = requests.get(url, proxies=proxies)
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, "lxml")
    uls = soup.find_all("ul", class_="photo")
    print(uls)
    aa=''
    for web_url in uls:
        urls=','.join(re.findall(r'href=".*?"', str(web_url)))
        aa+=urls       
#     bb=' '.join(aa)
#     print(len(aa))
    #print(soup)
#     print(aa)

    url1=re.findall(r'".*?.html"', aa,re.RegexFlag.S)
    for urls in url1:
        spider_fetch(url+urls.strip('"'))

def spider_fetch(url):
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, "lxml")
    name_url=re.findall(r'<title>.*?</',soup.contents)
    name_str=name_url[0][7:-3]
    print(name_str)
    uls = soup.find_all("ul", class_="file")
    aa=[]
    i=1
    for web_url in uls:
        urls=re.findall(r'".*.jpg?"', str(web_url))
        aa+=urls
        
    for fetch_url in aa:          
        try:
            print(fetch_url)

            jpg=requests.get(fetch_url)
            if jpg.status_code!=200:
                continue
        #f=open('D:\\a'+str(i)+'.mp4','wb')
            with open('D:\\a' + str(i)+ '.jpg','wb') as f:
                f.write(jpg.content)
        
        except:
            continue
        else:
            i=i+1


if __name__ == "__main__":
    spider()
    os.system("pause")