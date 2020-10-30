# coding=utf-8

import requests
import time

url = ['https://www.taobotics.com/mini.html',
       'https://www.taobotics.com/stone.html',
       'https://www.taobotics.com/giraffe.html',
       'https://www.taobotics.com/chassis.html',
       'https://www.taobotics.com/other.html',
       'https://www.taobotics.com/education.html',
       'https://www.taobotics.com/retail.html',
       'https://www.taobotics.com/disinfection.html',
       'https://www.taobotics.com/inspection.html',
       'https://www.taobotics.com/index.html']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    ]
count = 0
countUrl = len(url)
print(headers.get('User-Agent'))
# 访问次数设置
# while count < 100:
#     try:  # 正常运行
#         for i in range(countUrl):
#             response = requests.get(url[i], headers=headers)
#             if response.status_code == 200:
#                 count = count + 1
#                 print('Success ' + str(count), 'times')
#         time.sleep(1800)
#
#     except Exception:  # 异常
#         print('Failed and Retry')
#         time.sleep(60)