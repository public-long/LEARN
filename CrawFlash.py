import requests
import os
import traceback



urlp = 'http://list.video.baidu.com/swf/ecomAdvPlayer.swf?tpl=coop&controls=progress,pause,volumn,fullscreen&video=http%3A%2F%2Fpgccdn.v.baidu.com%2F361892357_4116985185_20171009132536.mp4%3Fauthorization%3Dbce-auth-v1%252Fc308a72e7b874edd9115e4614e1d62f6%252F2017-10-09T05%253A25%253A40Z%252F-1%252F%252F3a34c3767008f786eb6cb50336678a61c9ee7ce2dbc4988430feb283ea2120d4%26responseCacheControl%3Dmax-age%253D8640000%26responseExpires%3DWed%252C%2B17%2BJan%2B2018%2B13%253A25%253A40%2BGMT%26xcode%3D367a31f160df35adf3e21e24a3af09135072a3227f4cc748%26time%3D1507647653'
url = 'http://list.video.baidu.com/swf/ecomAdvPlayer.swf?tpl=coop&controls=progress,pause,volumn,fullscreen&video=http%3A%2F%2Fpgccdn.v.baidu.com%2F379235422_431839690_20170307143629.mp4%3Fauthorization%3Dbce-auth-v1%252Fc308a72e7b874edd9115e4614e1d62f6%252F2017-03-07T06%253A40%253A22Z%252F-1%252F%252Ff124d7f031e3aa21de548eb222d8f7f0d200f6a655d3f1ebfeb23c42d742ccb6%26responseCacheControl%3Dmax-age%253D8640000%26responseExpires%3DThu%252C%2B15%2BJun%2B2017%2B14%253A40%253A22%2BGMT%26xcode%3D5d2ca5239b1ab7655102492728267fbf0085ea39e1a9b1df%26time%3D1507650266'
urlp,url = url,urlp
root = 'D://learning\webCrawler//picture//'
path = root + url.split('0')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    traceback.print_exc()
    print('爬取失败')
    
