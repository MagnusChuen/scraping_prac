import time
from selenium import webdriver
from bs4 import BeautifulSoup
import random
driver = webdriver.Chrome()
driver.get('https://user.qzone.qq.com/1934330968/infocenter?_t_=0.5621754646201798')
time.sleep(15)
driver.maximize_window()
time.sleep(3)
index = 1
def get_message(driver):
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    contents = bs.find_all('div', {'class': "f-info"})
    for content in contents:
        messages.add(content.get_text())

t = True
i = 1

messages = set()

while t:
    check_height = driver.execute_script("return document.body.scrollHeight;")
    m = random.uniform(10, 11)
    time.sleep(m)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(random.uniform(1, 2))
    get_message(driver)
    check_height1 = driver.execute_script("return document.body.scrollHeight;")
    if check_height == check_height1:
        t = False

driver.close()

with open('D://qq_space_2.txt', 'a', encoding='utf-8') as f:
    for x in messages:
        f.write(f'{x}\n')
