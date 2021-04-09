import time

from selenium import webdriver

wd = webdriver.Chrome('C:\\Users\\dpswp\\OneDrive\\바탕 화면\\교육\\파이썬_웹_DB\\chromedriver_win32\\chromedriver.exe')
wd.get("https://www.google.com")

time.sleep(3)
html = wd.page_source

print(html)

wd.close()