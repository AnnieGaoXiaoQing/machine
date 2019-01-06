#encoding=utf-8
import requests

def response():
    response = requests.get('https://api.github.com')
    print(response.status_code)
    print(response.reason)
    print(response.headers)
    print(response.url)  #https://api.github.com/
    print(response.history)  #默认为空，可访问http链接(会进行转接) [<Response [301]>]
    print(response.elapsed)  #响应时间
    print(response.encoding)
    print(response.content)  #内容
    print(response.text)
    print("json>>>>>>>>>>>>>>>")
    print(response.json())
    print(response.json()['team_url'])  #类似字典，直接取出

if __name__ == '__main__':
    response()
