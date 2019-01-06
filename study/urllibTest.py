# -*- coding:utf-8 -*-
from urllib.request import urlopen
import urllib.parse
import urllib.request

URL_IP = "http://baidu.com"
#https://cangzhou.58.com/house.shtml?utm_source=link&spm=u-Lj4SZGxa1luDubj.psy_jiugongge&PGTID=0d100000-0028-caac-a47d-ce977fab62a8&ClickID=2
URL_GET = "https://cangzhou.58.com/house.shtml/get"

def use_simple_urllib():
    response = urlopen(URL_IP)
    print(">>>>>>>Response headers:")
    print(response.info())
    print(">>>>>>>Response Body:")
    html = response.read().decode('utf-8')
    print(html)

def use_params_get():
    #构建请求参数
    params = urllib.parse.urlencode({'param1':'hello','param2':'world'})
    print('Request params:')
    print(params)

    #发送请求
    response = urlopen('?'.join([URL_GET,'%s']) % params)

    #处理响应
    print(">>>>>>>Response headers:")
    print(response.info())
    print(">>>>>>>Response Body:")
    html = response.read().decode('utf-8')
    print(html)


if __name__ == '__main__':
   # use_simple_urllib();
   use_params_get()