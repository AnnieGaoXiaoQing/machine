#encoding=utf-8
import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])

def basic_auth():
    """
    基本认证(不安全，密码可被破解)
    :return:
    """
    response = requests.get(construct_url('user'), auth=('imoocdemo','imoocdemo123'))
    print(response.text)
    print(response.headers)

if __name__ == '__main__':
    basic_auth()