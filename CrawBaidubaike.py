import requests
from bs4 import BeautifulSoup
import traceback
word = '王者荣耀'
#word = input('请输入词条:')
start_url = 'https://baike.baidu.com/item/'
#url = 'https://baike.baidu.com/item/小王子/270'
url = start_url + word
try:
    r = requests.get(url, timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    traceback.print_exc()
    
soup = BeautifulSoup(r.text, 'html.parser')
val = soup.find_all('div', attrs = {'class': 'para', 'label-module': 'para'})
for i in val:
    for j in i.descendants:
        if j.string is not None:
            print(j.string, end = '')
    print()
