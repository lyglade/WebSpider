# -*- coding:utf-8 -*-
import os
import requests
import re
from bs4 import BeautifulSoup

def spider():
    url = "http://www.airenti55.net/"
    #proxies = {"http": "http://172.17.18.80:8080", "https": "https://172.17.18.80:8080"}
    #r = requests.get(url, proxies=proxies)
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, "lxml")
    uls = soup.find_all("ul", class_="photo")
    print(uls)
    aa=[]
    for web_url in uls:
        urls=re.findall(r'href=".*?"', str(web_url))
        aa.append(urls)
        
          
    
    #print(soup)
    print(aa)

if __name__ == "__main__":
    spider()
    os.system("pause")