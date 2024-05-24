import time

import requests
session = requests.session()
cookies = {
    'Hm_lvt_696281423db202c79a687ee2dd8ed64d': '1716453472,1716466739',
    'first_h_kp': '1716467597912',
    'count_h_kp': '1',
    'first_m_kp': '1716467597914',
    'count_m_kp': '1',
    'Hm_lvt_0e27bf7b28bc37a749758efa835a8de4': '1716467598',
    'Hm_lpvt_0e27bf7b28bc37a749758efa835a8de4': '1716467598',
    'Hm_lvt_38ea8ed97fbe7c334fcc1878c579e5e0': '1716467598',
    'Hm_lpvt_38ea8ed97fbe7c334fcc1878c579e5e0': '1716467598',
    'Hm_lvt_c11e70df18184f7263176ce90c8a9cc3': '1716467599',
    'Hm_lpvt_c11e70df18184f7263176ce90c8a9cc3': '1716467599',
    'Hm_lpvt_696281423db202c79a687ee2dd8ed64d': '1716467712',
}
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'Hm_lvt_696281423db202c79a687ee2dd8ed64d=1716453472,1716466739; first_h_kp=1716467597912; count_h_kp=1; first_m_kp=1716467597914; count_m_kp=1; Hm_lvt_0e27bf7b28bc37a749758efa835a8de4=1716467598; Hm_lpvt_0e27bf7b28bc37a749758efa835a8de4=1716467598; Hm_lvt_38ea8ed97fbe7c334fcc1878c579e5e0=1716467598; Hm_lpvt_38ea8ed97fbe7c334fcc1878c579e5e0=1716467598; Hm_lvt_c11e70df18184f7263176ce90c8a9cc3=1716467599; Hm_lpvt_c11e70df18184f7263176ce90c8a9cc3=1716467599; Hm_lpvt_696281423db202c79a687ee2dd8ed64d=1716467712',
    'origin': 'https://www.70xi.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.70xi.com/yin/?name=%E6%A2%A6%E9%86%92%E6%97%B6%E5%88%86&type=qq',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
session.cookies.update(cookies)
session.headers.update(headers)
import os
try:
    os.mkdir('d://songs', mode=511, dir_fd=None)
except:
    pass

words = '我是这个程序的开发者阿飞，欢迎使用这个音乐采集器，使用该程序时请保持网络通畅，下好的歌曲请在d盘的songs文件夹中查看'
words_1 = '提醒：极少音乐链接被封禁或者转换可能无法播放'
print(words)
print(words_1)
print('----------------------------------------------------------')
song_name = input('请输入您要查询的歌曲名字')
while True:
    try:
        x = int(input('选择您要搜索的平台，网易云输1，qq音乐输2'))
    except:
        print('都说了叫你小子输入数字啊！！！')
    else:
        break
page_num = 1
if x == 1:
    source = 'netease'
elif x == 2:
    source = 'qq'
else:
    print('oops！ 你貌似输错了数字')
data = {
    'input': song_name,
    'filter': 'name',
    'type': source,
    'page': page_num,
}
def get_info():
    response = session.post('https://www.70xi.com/yin/', data=data).json()
    index = 1
    for x in response['data']:
        print('编号：' + str(index))
        print(x['title'])
        print(x['author'])
        print('下载链接：' + x['url'])
        print('----------------------------------------------------------')
        index += 1
    return response

def download(response):
    while True:
        m= int(input('请输入您要下载的歌曲编号'))
        if m in range(1, len(response['data'])+1):
            break
    print('\n下载链接为：' + response['data'][m-1]['url'])
    song = response['data'][m-1]['title'].replace('/', '')
    res = session.get(response['data'][m-1]['url'])
    res = res.content
    try:
        with open("d://songs/{}.mp3".format(song), 'wb')as f:
            f.write(res)
    except:
        print('oops，貌似你需要更改一下文件权限')
        print('请以管理员身份重新启动程序')
    else:
        print('\n下载成功!!!快去听这个该死的歌吧！！！')

res = get_info()
download(res)
i = True
while i:
    while True:
        try:
            x = int(input('继续在该列表下载请按1，跳转到下一页资源请按2，搜索其他歌曲请按3，退出请按4'))
        except:
            print('\n都说了叫你小子输入数字啊！！！')
        else:
            break
    if x == 1:
        download(res)
    elif x == 2:
        data['page'] += 1
        try:
            response = get_info()
        except:
            print('好像不行哦！！！')
        else:
            download(response)
    elif x == 3:
        data['input'] = input('请输入您要查询的歌曲名字')
        data['page'] = 1
        resp = get_info()
        download(resp)
    elif x == 4:
        print('\n你已退出，byebye！')
        time.sleep(3)
        i = False

    else:
        print('oops！ 你貌似输错了数字')







