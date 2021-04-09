from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from collection import crawler


def ex01():
    request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    response = urlopen(request)
    html = response.read().decode('cp949')
    #print(html)                   # 소스 긁어옴

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class' : 'tit3'})

    for index, div in enumerate(divs):
        print(index+1, div.a.text, div.a['href'], sep=':')  # div 블럭에서 a 태그가 감싸고 있는 텍스트를 가져옴, div.a['href'] 는 하이퍼링크도 가져옴
        # 찾은 div 블럭에서 a 태그를 가져옴 => div.a
        # sep은 데이터 찍으면서 중간에 구별하면서 나오는거

#ex01 을 함수로 만들어서 사용, crawler.py 에 있는거
def ex02():
    html = crawler.crawling(
        url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn",
        encoding= 'cp949')
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    for index, div in enumerate(divs):
        print(index + 1, div.a.text, div.a['href'], sep=':')


if __name__ == '__main__':
    #ex01()
    ex02()