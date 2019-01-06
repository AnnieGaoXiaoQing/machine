#encoding=utf-8
import json
import requests
from requests import exceptions

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL, endpoint])

#json解析信息
def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

#查看用户姓名信息
def request_method():
    response = requests.get(build_uri('users/imoocdemo'))
    print(better_print(response.text))

#获取用户邮件信息（需要账号和密码）
def request_email():
    response = requests.get(build_uri('users/emails'), auth=('imoocdemo','imoocdemo123'))
    print(better_print(response.text))

#获取指定id开始的用户信息
def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print(better_print(response.text))
    print(response.url)

#pathch:修改信息  post:添加信息
def json_request():
    #response = requests.patch(build_uri('user'),
    # auth = ('imoocdemo','imoocdemo123'),json={'name':"babymooc12"})
    #添加邮箱地址
    response = requests.post(build_uri('user/email'),
                             auth=('imoccdemo','imoocdemo123'),json=['helloworld@github.com'])
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

#异常处理
def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status() #显示抛异常
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        print(response.text)
        print(response.status_code)

def hard_requests():
    from requests import Request,Session
    s = Session()
    headers = {'User-Agent':'fake1.3.4'}
    req = Request('Get',build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),headers=headers)

    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)

    resp = s.send(prepped, timeout = 5)
    print(resp.status_code)
    print(resp.headers)
    print(resp.text)

if __name__ == '__main__':
    hard_requests()