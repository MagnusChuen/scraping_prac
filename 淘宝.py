'''纯手搓，暴力简单且好用，可以爬取指定关键词，指定页面数的商品信息。'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from bs4 import BeautifulSoup

search_name= input('输入你要搜索的内容')
demanded_page = input('你需要多少页的内容')
driver = webdriver.Chrome()

price_list = []
sale_list = []
name_list = []

js = 'window.scrollTo(0, document.body.scrollHeight)'

def get_price(bs):
    lis = bs.find_all('span', {'class': "Price--priceInt--ZlsSi_M"})
    for x in lis:
        price = x.get_text()
        price_list.append(price)

def get_sales(bs):
    lis_2 = bs.find_all('span', {'class': "Price--realSales--FhTZc7U"})
    for x in lis_2:
        real_sales = x.get_text().replace('人付款', '')
        sale_list.append(real_sales)

def get_names(bs):
    lis_3 = bs.find_all('div', {'class': "Title--title--jCOPvpf"})
    for x in lis_3:
        lis_4 = x.find_all('span', {'class': ""})
        for x in lis_4:
            name = x.get_text()
            if name != search_name:
                name_list.append(name)

def turn_to_next_page(driver):
    submit = driver.find_element(By.XPATH, '//*[@id="pageContent"]/div[1]/div[3]/div[4]/div/div/button[2]/span')
    submit.click()
    time.sleep(5)


def get_info(driver):
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    get_names(bs)
    get_price(bs)
    get_sales(bs)

index = 1

def main(driver):
    global index
    url = f'https://s.taobao.com/search?catId=100&from=sea_1_searchbutton&page={index}&q={search_name}&spm=a2141.241046-cn.searchbar.d_2_searchbox&tab=all&tmhkh5=&type=p'
    driver.get(url)
    time.sleep(10)
    driver.maximize_window()
    time.sleep(5)
    get_info(driver)
    while index < int(demanded_page):
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        driver.execute_script(js)
        time.sleep(5)
        turn_to_next_page(driver)
        get_info(driver)
        index += 1
    driver.close()

main(driver)
csv_file = open(f'D:/{search_name}_data.csv', 'w', newline='', encoding='gbk')
writer = csv.writer(csv_file)
writer.writerow(['product', 'price', 'sales'])
for name, price, sales in zip(name_list, price_list, sale_list):
    try:
        writer.writerow([name, price, sales])
    except UnicodeEncodeError:
        pass
csv_file.close()

print('完成（done）！！！')








