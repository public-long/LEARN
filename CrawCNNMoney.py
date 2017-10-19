import requests
from bs4 import BeautifulSoup
import traceback
import re

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
        tr = soup.find_all('tr')
        search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
        
        for i in range(len(tr)-2):
            infomation = re.findall(search_pattern, tr[i+2])
            print(infomation)
        
    except:
        traceback.print_exc()
            



#def printSocketList(ilt, path):


def main():
    url = 'http://money.cnn.com/data/dow30/'
    infoList = []
    path = 'D:\learning\webCrawler\CNNMoney.txt'
    try:
        html = getHTMLText(url)
        getSocketList(html, infoList)
    except:
        traceback.print_exc()
    #printSocketList(infoList, path)


main()
