# coding=utf-8
import _thread
import time
import urllib
from bs4 import BeautifulSoup
import requests
import random

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
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
]

# Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)

taobotics_url = [
    'https://www.taobotics.com/mini.html',
    'https://www.taobotics.com/stone.html',
    'https://www.taobotics.com/giraffe.html',
    'https://www.taobotics.com/chassis.html',
    'https://www.taobotics.com/other.html',
    'https://www.taobotics.com/education.html',
    'https://www.taobotics.com/retail.html',
    'https://www.taobotics.com/disinfection.html',
    'https://www.taobotics.com/inspection.html',
    'https://www.taobotics.com/index.html'
]
edu_url = [
    'https://edu.taobotics.com/',
    'https://edu.taobotics.com/categories/',
    'https://edu.taobotics.com/wiki/',
    'https://edu.taobotics.com/about/',
    'https://edu.taobotics.com/projects/',
    'https://edu.taobotics.com/2017/10/18/opencv-install/',
    'https://edu.taobotics.com/2017/10/17/gitpage/',
    'https://edu.taobotics.com/2017/10/10/ros-introduction/',
    'https://edu.taobotics.com/page2',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/1.1-Hardware-Check/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/0.1-Getting-Started/doc/index.html',
    'https://edu.taobotics.com/2017/09/26/markdown/',
    'https://edu.taobotics.com/2017/07/04/linux-swap/',
    'https://edu.taobotics.com/2017/05/16/cv-overview/',
    'https://edu.taobotics.com/2017/04/11/shadowsocks/',
    'https://edu.taobotics.com/2017/04/05/robotics-learning/',
    'https://edu.taobotics.com/2017/04/01/gitlab/',
    'https://edu.taobotics.com/about/README/index.html<priority>0.58</priority>',
    'https://edu.taobotics.com/wiki/Appendix/HandsFree_VS_Turtlebot/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/1.5-Environment-Config/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/3.2-AR-Marker-Detect/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/3.1-Vision-Case/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/3.3-Follow-AR-Marker/doc/index.html',
    'https://edu.taobotics.com/wiki/Hardware/Devices-Sensors/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/1.2-Remote-Your-Robot/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/2.1-Mapping/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/1.1-Install-Ubuntu/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/1.2-Windows-Install-Ubuntu/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/2.2-Navigation/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/5.1-Simulation/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Intermediate/3.3-Python-Navigation/doc/index.html',
    'https://edu.taobotics.com/wiki/OpenRE/README/index.html',
    'https://edu.taobotics.com/wiki/Hardware/OpenRE-Board/index.html',
    'https://edu.taobotics.com/wiki/FAQ/2.1-Hardware-Error/doc/index.html',
    'https://edu.taobotics.com/2017/09/26/markdown',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/1.3-Important-Topics/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/4.2-Speech-Control/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Beginner/5.2-Android-App/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Intermediate/3.1-Python-Get-Sensors/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Intermediate/3.2-Python-Base-Control/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Intermediate/3.6-Python-Application-Patrol/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Intermediate/3.5-Python-Advance-App/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Advanced/VSLAM-RGBD-SLAM/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Advanced/Behavior-Tree/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Advanced/Object-Recognition/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Advanced/Person-Follower/doc/index.html',
    'https://edu.taobotics.com/wiki/Tutorial/Advanced/Object-Pick-Place/doc/index.html',
    'https://edu.taobotics.com/wiki/OpenRE/Getting-Started/index.html',
    'https://edu.taobotics.com/wiki/OpenRE/Architecture/index.html',
    'https://edu.taobotics.com/wiki/OpenRE/Develop/index.html',
    'https://edu.taobotics.com/wiki/OpenRE/HFLink/index.html',
    'https://edu.taobotics.com/wiki/Hardware/Power-Manager/index.html',
    'https://edu.taobotics.com/wiki/Hardware/Module/index.html',
    'https://edu.taobotics.com/wiki/Appendix/Robotics_Learning/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/1.3-Remote-Terminal/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/1.4-Remote-Desktop/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/1.6-Get-IP/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/3.1-When-USB-Broken/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/3.3-OpenRE-Error/doc/index.html',
    'https://edu.taobotics.com/wiki/FAQ/3.2-When-Motor-Interface-Broken/doc/index.html',
    'https://edu.taobotics.com/about/Project-Overview/index.html',
    'https://edu.taobotics.com/about/About-US/index.html',
    'https://edu.taobotics.com/about/Why-HandsFree/index.html',
    'https://edu.taobotics.com/about/Story-And-Wine/index.html'
]

def get_ip_list(url):
    ip_list = []
    for i in range(1, 5):
        web_data = requests.get(url + str(i), user_agent_list[6])
        features = "html.parser"
        soup = BeautifulSoup(web_data.text, features=features)

        ips = soup.find_all('tr')
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[0].text + ':' + tds[1].text)
        time.sleep(3)
    # 检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
            proxy_host = "https://" + ip
            # print(proxy_host)
            proxy_temp = {"https": proxy_host}
            res = urllib.urlopen(url, proxies=proxy_temp).read()
        except Exception as e:
            ip_list.remove(ip)
            continue
    return ip_list

# 从ip池中随机获取ip列表
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

# 为线程定义一个函数
def print_time(threadName, delay, headers,ip_list):
    proxies = get_random_ip(ip_list)
    count = 0
    countUrl = len(taobotics_url)
    while count < 100:
        time.sleep(delay)
        print(headers)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        try:  # 正常运行
            for i in range(countUrl):
                response = requests.get(taobotics_url[i], proxies=proxies, headers=headers)
                if response.status_code == 200:
                    count = count + 1
                    print('Success ' + str(count), 'times', '本次使用代理为：',proxies)
                    time.sleep(60 * 0.5)
            # time.sleep(60*60*2)  # 秒-分-时
        except Exception:  # 异常
            print('Error:访问错误,可能是代理错误。')
            time.sleep(60)
# 创建两个线程
try:
    for i in range(0, len(user_agent_list)-1):
        url = 'https://www.kuaidaili.com/free/inha/'
        ip_list = get_ip_list(url)
        _thread.start_new_thread(print_time, ("Thread-" + str(i ), 60 * i, user_agent_list[i],ip_list))
except:
    print('Error: 无法启动线程')

while 1:
    pass
