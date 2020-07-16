"""
날짜 : 2020/07/16
이름 : 김철학
내용 : 파이썬 네이버 영화 리뷰평점 데이터 수집하기
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime

#크롬 가상브라우저 실행
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#browser = webdriver.Chrome('../Ch01/chromedriver.exe', chrome_options=chrome_options)
browser = webdriver.Chrome('../Ch01/chromedriver.exe')
browser.implicitly_wait(3)

#네이버 영화 랭킹 평점순 이동
browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt')
browser.implicitly_wait(3)

#영화 랭킹 1위 클릭
rank1 = browser.find_element_by_css_selector('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
rank1.click()
browser.implicitly_wait(3)

#영화 평점 탭 클릭
review_tab = browser.find_element_by_css_selector('#movieEndTabMenu > li:nth-child(5) > a')
review_tab.click()
browser.implicitly_wait(3)

# iframe 전환
browser.switch_to_frame('pointAfterListIframe')
browser.implicitly_wait(3)

# 평점, 리뷰, 날짜 수집
scores  = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li > div.star_score > em')
reviews = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li > div.score_reple > p > span')
dates   = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li > div.score_reple > dl > dt > em:nth-child(2)')

print(scores[9].text)

print('종료...')
#브라우저 종료
browser.close()

"""
#디렉터리 생성
dir = "/home/bigdata/naver/naver-{:%y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
	os.makedirs(dir)

#파일로 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf8')

file.write('순위,제목,날짜\n')

for item in item_boxs:
    file.write('%s,' % item.find_element_by_css_selector('.item_num').text)
    file.write('[%s],' % item.find_element_by_css_selector('.item_title_wrap > .item_title').text)
    file.write('%s\n' % "{:%y%m%d%H%M%S}".format(datetime.now()))

#파일닫기
file.close()


"""
