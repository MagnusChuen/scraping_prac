#继上一个手动爬取笔趣阁小说的版本后，又写了一个一口气爬取该网站所有小说并打包储存好的程序。因水平有限，所以比较臃肿且速度有些许感人，好在运行起来畅通无阻。恳请各位大佬指导
import re
import urllib.request
from urllib import request
from bs4 import BeautifulSoup
import time
import os
#get fiction names of a certain sort page
fiction_name_list = []
fiction_link_list = []
links = set()

#get fiction links of a certain sort page
def get_link(pageurl):
    link_list = []
    headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}
    request = urllib.request.Request(url=pageurl, headers=headers)
    html = urllib.request.urlopen(request)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('span', {'class': 'jie'}):
        link = 'https://www.biquge365.net/' + link.find('a').attrs['href']
        link_list.append(link)
    return link_list

def get_next_page_link(pageurl):
    headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}
    request = urllib.request.Request(url=pageurl, headers=headers)
    html = urllib.request.urlopen(request)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('div', {'class': 'page'}):
        link = 'https://www.biquge365.net/' + link.find('a').attrs['href']
        if link == f'https://www.biquge365.net//sort/1_1/':
            link = None
        elif link == f'https://www.biquge365.net//sort/2_1/':
            link = None
        elif link == f'https://www.biquge365.net//sort/3_1/':
            link = None
        elif link == f'https://www.biquge365.net//sort/4_1/':
            link = None
        elif link == f'https://www.biquge365.net//sort/5_1/':
            link = None
        elif link == f'https://www.biquge365.net//sort/6_1/':
            link = None
        elif link == f'https://www.biquge365.net//sort/7_1/':
            link = None
        elif link == f'https://www.biquge365.net//sort/8_1/':
            link = None
    return link

def get_articles(articleurl):
    url = articleurl
    headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}
    request = urllib.request.Request(headers=headers, url=url)
    html = urllib.request.urlopen(request)
    bs = BeautifulSoup(html, 'html.parser')
    contents = bs.find_all('div', {'id': 'txt', 'class': 'txt'})
    try:
        name_2 = bs.find_all('meta', {'name': 'keywords'})[0].attrs['content']
    except Exception:
        pass
    if contents != []:
        new_link = 'https://www.biquge365.net/' + bs.find_all('li')[15].a.attrs['href']
        name_1 = bs.find_all('meta', {'name': 'keywords'})[0].attrs['content'].split(',')[0]
        name_2 = bs.find_all('meta', {'name': 'keywords'})[0].attrs['content']
        path = 'D:/fiction'
        os.chdir(path)
        new_folder = name_1
        try:
            os.makedirs(new_folder)
        except FileExistsError:
            with open(f'D:/fiction/{name_1}/{name_2}.txt', 'w', encoding='utf-8') as f:
                for content in contents:
                    content = content.get_text().replace('一秒记住【笔趣阁】biquge365.net，更新快，无弹窗！', '')
                    f.write(content.strip())
            try:
                get_articles(new_link)
            except WindowsError:
                get_articles(new_link)
        else:
            with open(f'D:/fiction/{name_1}/{name_2}.txt', 'w', encoding='utf-8') as f:
                for content in contents:
                    content = content.get_text().replace('一秒记住【笔趣阁】biquge365.net，更新快，无弹窗！', '')
                    f.write(content.strip())
            try:
                get_articles(new_link)
            except WindowsError:
                get_articles(new_link)
    else:
        print(f"f'{name_2}' done")

def get_fiction(pageurl):
    try:
        link_list = get_link(pageurl)
        next_page_link = get_next_page_link(pageurl)
    except WindowsError:
        get_fiction(pageurl)
    else:
        for link in link_list:
            if link not in links:
                get_articles(link)
                links.add(link)
        try:
            time.sleep(1)
            get_fiction(pageurl)
        except ValueError:
            print('done!')

sort_page_1 = 'https://www.biquge365.net/sort/1_1/'
sort_page_2 = 'https://www.biquge365.net/sort/2_1/'
sort_page_3 = 'https://www.biquge365.net/sort/3_1/'
sort_page_4 = 'https://www.biquge365.net/sort/4_1/'
sort_page_5 = 'https://www.biquge365.net/sort/5_1/'
sort_page_6 = 'https://www.biquge365.net/sort/6_1/'
sort_page_7 = 'https://www.biquge365.net/sort/7_1/'
sort_page_8 = 'https://www.biquge365.net/sort/8_1/'
sort_page_list = [sort_page_1, sort_page_2, sort_page_3, sort_page_4, sort_page_5, sort_page_6, sort_page_7, sort_page_8]

for sort_page in sort_page_list:
    get_fiction(sort_page)









