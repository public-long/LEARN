# -*- coding: utf-8 -*-

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)   #用正则表达式获取"view_price"字符段
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price, title])

    except:
        print ("")

def printGoodsList(ilt):
    path = "D://learning//webCrawler//袜子女.txt"
    tplt = "{:4}\t{:8}\t{:16}"
    with open(path, "w") as f:
        f.write(tplt.format("序号", "价格", "商品名称") + '\n')
        count = 0
        for g in ilt:
            count = count +1
            #print(tplt.format(count, g[0], g[1]))
            f.write(tplt.format(count, g[0], g[1]) + '\n')
        f.close

def main():
    goods = '袜子女'
    depth = 3
    print("ok'")
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
main()
