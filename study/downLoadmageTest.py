#encoding=utf-8
import requests
import os

#缺点：流一直未关闭
def download_image():
    """ 下载图片，文件
    :return:
    """
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}  #指定浏览器打开
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1546744937266&di=35e29743eab002dff12e0cb568590825&imgtype=0&src=http%3A%2F%2Fimg.article.pchome.net%2F00%2F28%2F19%2F00%2Fpic_lib%2Fwm%2Flyckpbz_36.jpg"
    response = requests.get(url,headers = headers,stream = True)

    with open(os.path.abspath(os.path.dirname(os.getcwd())) + "/data/demo.jpg",'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


#优化版：关闭流
def download_image_improve():
    #伪造headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}  # 指定浏览器打开
    #限定url
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1546744937266&di=35e29743eab002dff12e0cb568590825&imgtype=0&src=http%3A%2F%2Fimg.article.pchome.net%2F00%2F28%2F19%2F00%2Fpic_lib%2Fwm%2Flyckpbz_36.jpg"

    from contextlib import closing
    with closing(requests.get(url,headers = headers, stream = True))  as response:
        #打开文件
        with open(os.path.abspath(os.path.dirname(os.getcwd())) + "/data/demo1.jpg",'wb') as fd:
            #每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)

if __name__ == '__main__':
    download_image_improve()