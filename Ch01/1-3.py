"""
날짜 : 2020/07/13
이름 : 김철학
내용 : 파이썬 네이버 헤드라인 뉴스 파싱하기
"""
from bs4 import BeautifulSoup as bs
import urllib.request as req

html = req.urlopen('https://datalab.naver.com/keyword/realtimeList.naver?where=main').read()

dom = bs(html, 'html.parser')

news_titles = dom.select('#section_it > .com_list > div > ul > li > a > strong')

for tit in news_titles:
    print(tit.string)

