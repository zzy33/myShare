#! -*- encoding:utf-8 -*-
import requests
import random

# 要访问的目标页面
targetUrl = "http://httpbin.org/ip"
# 要访问的目标HTTPS页面
# targetUrl = "https://httpbin.org/ip"
# 代理服务器
proxyHost = "t.16yun.cn"
proxyPort = "31111"
# 代理隧道验证信息
proxyUser = "16ZKBRLB"
proxyPass = "234076"
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}
# 设置 http和https访问都是用HTTP代理
proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}
# 设置IP切换头
tunnel = random.randint(1, 10000)
headers = {"Proxy-Tunnel": str(tunnel)}
resp = requests.get(targetUrl, proxies=proxies, headers=headers)
print(resp.status_code)
print(resp.text)
# import urllib2
# import socket
# import time
# import random
# import BeautifulSoup
#
# '''
# 代理池网址：https://www.xicidaili.com/wt
# 函数功能：通过爬虫爬取代理池网站中的ip:port并写入一个名为proxy的文本中
# '''
#
#
# def get_IPlist():
#     User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
#     header = {}
#     header['User-Agent'] = User_Agent
#     url = 'http://www.66ip.cn/areaindex_1/1.html'
#     # url = 'https://www.xicidaili.com/wt/' + str(random.randint(1, 6))  # 1-6页随机选择一页
#     req = urllib2.Request(url, headers=header)
#     res = urllib2.urlopen(req).read()
#
#     soup = BeautifulSoup.BeautifulSoup(res)
#     ips = soup.findAll('tr')
#     # f = open(proxy, w)
#     with open(./proxy, 'w') as f:
#         for x in range(1, len(ips)):
#             ip = ips[x]
#
#             tds = ip.findAll(td)
#             ip_temp = tds[1].contents[0] + , + tds[2].contents[0] + \n
#
#             print
#             tds[1].contents[0] + \t + tds[2].contents[0]
#             f.write(ip_temp)
#     print(url)
#     print(获取代理IP列表成功！)
#     time.sleep(3)
#
#
# def main():
#     socket.setdefaulttimeout(3)  # 当爬取超过3秒时略过本次操作 防止程序卡住
#     # 报头信息列表
#     user_agent_list = [
#         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#         'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
#         'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#         'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#         'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
#         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
#         'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#         'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
#         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
#         'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
#         'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#     ]
#     f = open(proxy)
#     lines = f.readlines()
#     proxys = []
#
#     for i in range(0, len(lines)):
#         ip = lines[i].strip().split(,)
#         proxy_host = http:// + ip[0] + : + ip[1]
#         # print (http://+ip[0]+:+ip[1])
#         proxy_temp = {http: proxy_host}
#         proxys.append(proxy_temp)
#     # 设置要刷访问量的网页
#     urls = {http://www.baidu.com}
#
#     sucess_times = 1
#     # for i in range(100):
#     for proxy in proxys:
#         for url in urls:
#             try:
#                 user_agent = random.choice(user_agent_list)
#                 proxy_support = urllib2.ProxyHandler(proxy)
#                 opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
#                 urllib2.install_opener(opener)
#                 req = urllib2.Request(url)
#                 c = urllib2.urlopen(req)
#                 print(sucessful, sucess_times)
#                 sucess_times += 1
#                 time.sleep(5)
#             except Exception, e:
#                 print proxy
#                 print e
#                 continue
#     print(已成功次数为%s % sucess_times)
#
#
# if __name__ == __main__:
#     get_IPlist()
#     main()