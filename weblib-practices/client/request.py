from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET

http_response = urlopen('https://www.example.com')
body = http_response.read()
body = body.decode('utf-8') # 이케 하면 이쁘게 뜸, 크롤링은 여기서 관심 있는 데이터를 뽑아내는 것

print(body)

print("=========================================================")

# POST

data = {
    'id' : 'seongho',
    'name' : '전성호',
    'pw' : '1234'
}

data = urlencode(data).encode('utf-8')

request = Request('https://www.example.com', data)
request.add_header('Content-Type', 'text/html')

http_response = urlopen(request)
print(http_response.status, http_response.reason)

body = http_response.read()
html = body.decode('utf-8')
print (html)