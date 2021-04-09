from bs4 import BeautifulSoup

html = '''
<td class="title black">
    <div class="tit3" data-no = "10">
        <a href="/movie/bi/mi/basic.nhn?code=189075" title="자산어보">자산어보</a>
    </div>
</td>'''


# 1. tag 조회
def ex01():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)

    tag_td = bs.td
    # print(tag_td)

    # tag_a = bs.a
    tag_a = tag_td.a
    print(tag_a)

    # None
    tag_h1 = bs.td.h1
    print(tag_h1)


# 2. attribute로 조회하기
def ex02():
    bs = BeautifulSoup(html, 'html.parser')
    #tag_td = bs.find('td', attrs={'class':'title'})    # td 태그를 찾는데, 클래스가 title 이 들어간 애들만 찾음
    tag_td = bs.find('td', attrs={'class': ['title','black']}) #이러면 클래스에 title이랑 balck 이 들어간 애들을 찾음
    print(tag_td)

    print("=====================")

    tag_div = bs.find('div', attrs={'class' : 'tit3', 'data-no' : '10'})  # 얘도 div 태그인데 클래스가 tit3, data-no 가 10인 애들
    print(tag_div)

if __name__ == '__main__':
    #ex01()
    ex02()