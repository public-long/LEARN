import requests
from bs4 import BeautifulSoup
import traceback
import re

'''
for i in range(10):
    r = requests.get('https://book.douban.com/subject/20443559/comments/hot?p='+str(i+1))
    soup = BeautifulSoup(r.text, 'lxml')
    p = soup.find_all('p',attrs = {'class':'comment-content'})
    for item in p:
        print(item.string)
'''

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()
        return(' ')

def parsePage(html,ilt):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        coms = soup.find_all('p', attrs = {'class': 'comment-content'})
        score_s = re.compile(r'span class="user-stars allstar(.*?) rating"')
        score = re.findall(score_s, html)
        for i in range(len(score)):
            com = coms[i].string[:10]
            #sco = re.search(r'\d{1,2}', score[i])
            ilt.append([com, int(score[i])])
    except:
        traceback.print_exc()

def printInfo(ilt, path):
    with open(path, 'w+') as f:
        count = 0
        for i in ilt:
            count = count + 1
            print(str(count)+' '+i[0]+' '+str(i[1]))
            f.writelines(str(count)+' '+i[0]+' '+str(i[1])+'\n')
    f.close

def main():
    depth = 2
   
    start_url = 'https://book.douban.com/subject/20443559/comments/hot?p='
    infoList = []
    path = "D:\learning\webCrawler\doubanBook.txt"
    for i in range(depth):
        try:
            url = start_url + str(i + 1)
            html = getHTMLText(url)
            parsePage(html, infoList)
        except:
            continue
    printInfo(infoList, path)

main()
    
