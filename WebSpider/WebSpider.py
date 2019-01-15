# -*- coding:utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup

def spider():
    url = "http://bj.grfy.net/"
    #proxies = {"http": "http://172.17.18.80:8080", "https": "https://172.17.18.80:8080"}
    #r = requests.get(url, proxies=proxies)
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all("div", class_="content")  
    print(len(divs))
    #print(soup)
    print(divs)

if __name__ == "__main__":
    spider()
    os.system("pause")