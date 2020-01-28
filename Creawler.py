# coding:utf-8
import requests
import json

query = '王祖贤'
''' 下载图片 '''
picpath = '/Users/amy/Downloads/宫崎骏电影海报'

def download(src, id):
    dir = picpath+'/' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


''' for 循环 请求全部的 url '''
for i in range(0, 25509, 20):
    url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
    html = requests.get(url).text
    response = json.loads(html, encoding='utf-8')
    print(type(response))
    for image in response['images']:
        print(image['src'])
        download(image['src'], image['id'])