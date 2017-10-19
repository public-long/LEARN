import requests
from bs4 import BeautifulSoup
import traceback
import re
import traceback

def getHTMLText(url):
     try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
     except:
        traceback.print_exc()
        return(' ')

def getSocketList(html, ilt):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        prices = re.compile(r'<span class="book-price">¥<i>(.*?)</i></span>')
        price = re.findall(prices, html)
        names = soup.find_all('h3')
        informations = soup.find_all('div', attrs = {'class': 'book-quote'})
        for i in range(len(names)):
            information = informations[i].find('p')
            ilt.append([price[i], names[i].string, information.string])
    except:
        traceback.print_exc()

def printSocketList(ilt, path):
    try:
        with open(path, 'w') as f:
            count = 0
            for i in ilt:
                count = count + 1
                print(str(count) + ' ' + '￥' + str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))
                f.writelines(str(count) + ' ' + '￥' +  str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + '\n')
        f.close
    except:
        traceback.print_exc()

def main():
    start_url = 'https://market.douban.com/book/?utm_campaign=book_freyr_section&utm_source=douban&utm_medium=pc_web&page='
    infoList = []
    depth = 2
    path = 'D:\learning\webCrawler\doubanBookshop.txt'
    for i in range(depth):
        try:
            url = start_url + str(i + 1)
            html = getHTMLText(url)
            getSocketList(html, infoList)
        except:
            continue
        printSocketList(infoList, path)


main()
        
