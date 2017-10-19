import requests
from bs4 import BeautifulSoup
import re
import traceback


addition = '²Ù×÷ÏµÍ³'
url = 'https://baike.baidu.com/item/'
start_url = url + addition
try:
    html = requests.get(atart_url, timeout = 30)
    html.raise_for_status()
    html.encoding = html.apparent_encoding
except:
    traceback.print_exc()
    continue

soup = BeautifulSoup(html, 'html.parser')
div = soup.find_all('div', attrs = {'class': 'para', 'label-module': 'para'})
