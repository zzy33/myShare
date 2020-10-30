# coding=utf-8
import _thread
import time
import requests

user_agent_list = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '},
    {'User-Agent': 'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}]

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

# 为线程定义一个函数
def print_time(threadName, delay, headers):
    count = 0
    countUrl = len(url)
    while count < 100:
        time.sleep(delay)
        print(headers)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        try:  # 正常运行
            for i in range(countUrl):
                proxies={'http': 'http://113.121.39.225:9999'}
                response = requests.get(url[i],proxies=proxies, headers=headers)
                if response.status_code == 200:
                    count = count + 1
                    print('Success ' + str(count), 'times')
                    time.sleep(60)
            # time.sleep(60*60*2)  # 秒-分-时
        except Exception:  # 异常
            print('Error:访问错误')
            time.sleep(60)
# 创建两个线程
try:
    for i in range(0, len(user_agent_list)-1):
        _thread.start_new_thread(print_time, ("Thread-" + str(i), 60 * i, user_agent_list[i]))

except:
    print('Error: 无法启动线程')

while 1:
    pass
