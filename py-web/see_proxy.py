# import requests
# from bs4 import BeautifulSoup
# def proxy():
#     url = 'http://httpbin.org/get'
#     r=requests.get(url)
#     print(r.text)
# if __name__ =='__main__':
#     proxy()

import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
def proxy():
    # url = 'http://httpbin.org/ip'
    # url = 'http://httpbin.org/get'
    url = 'https://icanhazip.com'
    proxies ={'https': 'https://175.43.156.16:9999'}
    r=requests.get(url, proxies = proxies, headers=headers)
    r.encoding = 'utf-8'
    print(r.text)
if __name__ =='__main__':
    proxy()