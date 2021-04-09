from datetime import datetime
from itertools import count
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from collection import crawler
import time

def crawling_pelicana():
    results = []

    for index in count(start=1, step=1):
        url = f"https://pelicana.co.kr/store/stroe_search.html?page={index}&branch_name=&gu=&si="
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_tables = bs.find('table', attrs={'class' : ['table','mt20']})
        tag_tbody = tag_tables.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            #tag_tr.strings # <tr> 에 있는거 텍스트만 남기고 리스트에 넣어줌
            datas = list(tag_tr.strings)

            name = datas[1]
            address = datas[3]
            sidogugun = address.split()[:2]

            t = (name,address) + tuple(sidogugun)
            results.append(t)

    # 저장
    table = pd.DataFrame(results, columns=['name','address','sido','gugun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8',mode='w',index=True)

def crawling_nene():
    pass

def crawling_kyochon():
    pass

def crawling_goobne():

    # Chrome 브라우저 시작
    url = "http://goobne.co.kr/store/search_store.jsp"
    wd = webdriver.Chrome('C:\\Users\\dpswp\\OneDrive\\바탕 화면\\교육\\파이썬_웹_DB\\chromedriver_win32\\chromedriver.exe')

    # 페이지 이동
    wd.get(url)
    time.sleep(3)

    results = []

    for index in count(start=1,step=1):
        # 자바 스크립트 실행
        script = f'store.getList({index})'
        wd.execute_script(script)
        print(f'{datetime.now()}: success for request[{script}]')
        time.sleep(3)

        # 자바스크립트 실행된 html(동적으로 렌더링 된 html) 가져오기
        html = wd.page_source

        # parsing 하기( bs4)
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id':'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if tags_tr[0].get('class') is None: # 클래스의 값을 가지고 올 수 있음
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)
            name = datas[1]
            address = datas[6]
            sidogugun = address.split()[:2]

            t = (name, address) + tuple(sidogugun)
            results.append(t)

    print(results)

    # 브라우저 닫기
    wd.close()

    #저장
    table = pd.DataFrame(results, columns=['name','address','sido','gugun'])
    table.to_csv('results/goobne.csv', encoding='utf-8',mode='w',index=True)

if __name__ == '__main__':
    #crawling_pelicana()
    crawling_goobne()