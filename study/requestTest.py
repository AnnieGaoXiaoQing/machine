# -*- coding:utf-8 -*-
import requests


URL_IP = "http://baidu.com"
#https://cangzhou.58.com/house.shtml?utm_source=link&spm=u-Lj4SZGxa1luDubj.psy_jiugongge&PGTID=0d100000-0028-caac-a47d-ce977fab62a8&ClickID=2
URL_GET = "https://cangzhou.58.com/house.shtml"
"""
def use_simple_request():
    response = requests.get(URL_IP)
    print(">>>>>>>Response headers:")
    print(response.headers)
    print(">>>>>>>Response Body:")
    print(response.text)
"""

def use_params_requests():
    #构建请求参数
    params = {'param1':'hello','param2':'world'}

    #发送请求
    response = requests.get(URL_GET,params=params)

    #处理响应
    print(">>>>>>>Response headers:")
    print(response.headers)
    print(">>>>>>>Response status_code:")
    print(response.status_code)
    print(response.reason)
    print(">>>>>>>Response Body:")
    print(response.text)

if __name__ == '__main__':
   #use_simple_request()
   use_params_requests()