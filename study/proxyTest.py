#encoding=utf-8
import requests


def proxy():
    proxies = {'http':'socks5://127.0.0.1:1080','https':'sock5:127.0.0.1:1080'}
    url = {'https://www.facebook.com'}
    response = requests.get(url,proxies=proxies,timeout = 10)
    print(response.status_code)

if __name__ == '__main__':
    proxy()