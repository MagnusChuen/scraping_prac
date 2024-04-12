#先导入所用使用的库
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re
import time

#设置一个空集合来储存获取到的链接，并发挥去重的功能
pages = set()

#定义函数
def get_links(pageurl):
    global pages
    try:
        html = urlopen('http://en.wikipedia.org{}'.format(pageurl))  #以防有些页面的错误请求，添加异常捕获
    except HTTPError:
        print('something wrong with the page, but do not worry')
    else:
        bs = BeautifulSoup(html, 'html.parser')
        for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    new_page = link.attrs['href']
                    print(new_page)
                    pages.add(new_page)
                    time.sleep(1)  #一定要设置请求间隔，否则可能返回502 gatewayerror
                    get_links(new_page)


#设置空参，从主页开始抓取
get_links('')