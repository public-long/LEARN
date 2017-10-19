# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

def  fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])


def printUnivList(ulist, num):
    path = 'D:\learning\webCrawler//univList_4.txt'
    #tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    with open(path, "w") as f:
        f.write( "{0:^10}\t{1:{3}^20}\t{2:^10}".format("排名", "学校名称", "总分", chr(97))+'\n')
        for i in range(num):
            u = ulist[i]
            f.write( "{0:^10}\t{1:{3}^20}\t{2:^10}".format(u[0], u[1], u[2], chr(97))+'\n')
        f.close
       
    #print "{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分")
    #for i in range(num):
    #     u = ulist[i]
    #    print "{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2])


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
    print("ok")
main( )
    
