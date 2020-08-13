"""
날짜 : 2020/07/15
이름 : 김철학
내용 : 파이썬 기상청 날씨 데이터 크롤링하기
"""
import os
import requests as req
from datetime import datetime
from bs4 import BeautifulSoup as bs

#세션시작
sess = req.session()

# 날씨 데이터 요청
html = sess.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')

#파싱
dom = bs(html.text, 'html.parser')

# 지역, 시정, 현재기온, 이슬점온도, 체감온도, 일강수, 습도, 풍향, 해면기압
locals = dom.select('#content_weather > table > tbody > tr > td > a')
visibilities = dom.select('#content_weather > table > tbody > tr > td:nth-child(3)')
temps = dom.select('#content_weather > table > tbody > tr > td:nth-child(6)')
dews = dom.select('#content_weather > table > tbody > tr > td:nth-child(7)')
sens_temps = dom.select('#content_weather > table > tbody > tr > td:nth-child(8)')
precipitations = dom.select('#content_weather > table > tbody > tr > td:nth-child(9)')
humidities = dom.select('#content_weather > table > tbody > tr > td:nth-child(10)')
direction_winds = dom.select('#content_weather > table > tbody > tr > td:nth-child(11)')
sea_pressures = dom.select('#content_weather > table > tbody > tr > td:nth-child(13)')

# 저장 디렉터리 생성
dir = '/home/bigdata/weather/weather-{:%y-%m-%d}'.format(datetime.now())
if not os.path.exists(dir):
    os.mkdir(dir)

# 파일로 저장 '20-07-15-16.csv'
fname = "{:%y-%m-%d-%H}.csv".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf8')

# csv파일 헤더
file.write('지역,시정,현재기온,이슬점온도,체감온도,일강수,습도,풍향,해면기압\n')

for i in range(0, len(locals)):
    rs1 = locals[i].text
    rs2 = visibilities[i].text if visibilities[i].text.strip() else 'NA'
    rs3 = dews[i].text if dews[i].text.strip() else 'NA'
    rs4 = sens_temps[i].text if sens_temps[i].text.strip() else 'NA'
    rs5 = precipitations[i].text if precipitations[i].text.strip() else 'NA'
    rs6 = humidities[i].text if humidities[i].text.strip() else 'NA'
    rs7 = direction_winds[i].text if direction_winds[i].text.strip() else 'NA'
    rs8 = sea_pressures[i].text if sea_pressures[i].text.strip() else 'NA'

    file.write(rs1+','+
               rs2+','+
               rs3+','+
               rs4+','+
               rs5+','+
               rs6+','+
               rs7+','+
               rs8+'\n')


file.close()
sess.close()

#cron작업 등록
#crontab -e
# * * * * * python3 /root/naver.py
#(분, 시, 일, 월, 요일)
#매분마다 python3 /root/naver.py 을 실행

#cron데몬 서비스 시작/종료
#systemctl start crond
#systemctl stop crond

#cron작업 조회
#crentab -l

#cron작업 삭제
#crentab -r


