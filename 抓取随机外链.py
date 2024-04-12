#导入所需要的库
from urllib.request import urlopen, HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random
import time
import datetime

#设置随机数种子以及空集合来储存页面链接
random.seed()

#定义函数获取页面所有内链
def get_internal_links(bs, includeurl):
    includeurl = '{}://{}'.format(urlparse(includeurl).scheme, urlparse(includeurl).netloc)
    internal_links = []
    #找所有以'/'开头的链接
    for link in bs.find_all('a', href = re.compile('^(/|.*'+includeurl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                if(link.attrs['href'].startswith('/')):
                    internal_links.append(includeurl+link.attrs['href'])
                else:
                    internal_links.append(link.attrs['href'])
    return internal_links

#定义函数获取页面所有外链
def get_external_links(bs, exclude_url):
    external_links = []
    for link in bs.find_all('a', href = re.compile('^(http|www)((?!'+exclude_url+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])
    return  external_links

#定义函数获取随机外链
def get_random_external_links(starting_page):
    if starting_page.startswith('https://') == False:
        starting_page = 'https://' +starting_page
    try:
        html = urlopen(starting_page)
    except HTTPError:
        print('something wrong with the page, but do not worry')
    else:
        try:
            bs = BeautifulSoup(html, 'html.parser')
        except decoding_error:
            print('something wrong with the page, but do not worry')
        else:
            external_links = get_external_links(bs, urlparse(starting_page).netloc)
            if len(external_links) == 0:
                print('no external links, looking at the site for one')
                domain = '{}://{}'.format(urlparse(starting_page).scheme, urlparse(starting_page).netloc)
                internal_links = get_internal_links(bs, domain)
                return get_random_external_links(internal_links[random.randint(0, len(internal_links)-1)])
            else:
                return external_links[random.randint(0, len(external_links)-1)]


#定义函数执行该过程
def follow_external_only(starting_page):
    external_link = get_random_external_links(starting_page)
    print('{}'.format(external_link))
    time.sleep(2)
    follow_external_only(external_link)



#运行试验
follow_external_only('https://www.wikipedia.org/')


