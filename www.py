import requests
import os
import traceback

for i in range(100):
    kw = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    url = 'http://img1.mm131.com/pic/3279/'+str(i + 1) +'.jpg'
    root = 'D://learning\webCrawler//picture//17//'
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url,headers = kw)
            #r.raise_for_status()
            if r.status_code != 200:
                print('��ȡ����')
                break
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print(str(i)+'�ļ�����ɹ�')
        else:
            print(str(i)+'�ļ��Ѵ���')
    except:
##        traceback.print_exc()
        print('��ȡʧ��')
    
