#手动版，需要输入域名
import urllib.request
from bs4 import BeautifulSoup
index = 1
def get_articles(articleUrl):
    global index
    url = 'https://www.biquge365.net' + f'{articleUrl}'
    headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}
    request = urllib.request.Request(headers=headers, url=url)
    html = urllib.request.urlopen(request)
    bs = BeautifulSoup(html, 'html.parser')
    contents = bs.find_all('div', {'id': 'txt', 'class': 'txt'})
    link_tag = bs.find_all('li')[18].a
    new_link = link_tag.attrs['href']
    while url != 'https://www.biquge365.net/book/69217/':
        #根据小说名更改储存文件名
        with open(f'D:/小说名/小说名_{index}.txt', 'w', encoding='utf-8') as f:
            for content in contents:
                content = content.get_text().replace('一秒记住【笔趣阁】biquge365.net，更新快，无弹窗！', '')
                f.write(content.strip())
        index += 1
        get_articles(new_link)

#输入第一章的路径/参数/锚点
get_articles('')
