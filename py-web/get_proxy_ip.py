# coding=utf-8
# IP地址取自国内高匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用
import _thread
import re
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
    web_data = requests.get(url, random.choice(user_agent_list))
    print(url)
    features = "html.parser"
    soup = BeautifulSoup(web_data.text, features=features)
    ips = soup.find_all('tr')
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        # print(tds)
        # ip_list.append(tds[3].text+'://'+tds[0].text + ':' + tds[1].text)
        ip=tds[0].text + ':' + tds[1].text
        ip_list.append(re.sub('[\r\n\t]', '', ip))
    return ip_list

def screen_ip_list(thread_name, proxy_url):
    ip_list = get_ip_list(proxy_url)
    print(ip_list)
    url = 'http://icanhazip.com'
    for ip in ip_list:
    #     try:
    #         proxy_host = "https://" + ip
    #         # print(proxy_host)
    #         proxy_temp = {"https": proxy_host}
    #         res = urllib.urlopen(url, proxies=proxy_temp).read()
    #         print(res)
    #     except Exception as e:
    #         ip_list.remove(ip)
    #         continue
    # print(ip_list)
    # return ip_list
        try:
            proxy_host = "http://" + ip
            proxy_temp = {"http": proxy_host}
            r = requests.get(url, proxies=proxy_temp, headers=random.choice(user_agent_list))
            r.encoding = 'utf-8'
            if r.status_code == 200:
                print(thread_name+":"+proxy_host+":success")
                for i in range(len(edu_url)):
                    requests.get(edu_url[i], proxies=proxy_temp, headers=random.choice(user_agent_list))
                    time.sleep(60 * 3)
        except Exception as e:
            print(thread_name+":"+proxy_host+":error")

try:
    for i in range(0, 15):
        # _thread.start_new_thread(screen_ip_list, ("Thread-" + str(i), 'http://www.ip3366.net/?stype='+str(i)+'&page='+str(i)))
        _thread.start_new_thread(screen_ip_list, ("Thread-" + str(i), 'https://www.89ip.cn/index_'+str(i+1)+'.html'))
        time.sleep(60)
except:
    print('Error: 无法启动线程')

while 1:
    pass


