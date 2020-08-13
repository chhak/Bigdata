"""
날짜 : 2020/08/11
이름 : 김철학
내용 : 선형회귀 분석 실습하기
"""

a = 0.9767441021911394
b = -102.209288612913

x_data = [170, 155, 150, 175, 165, 180, 182, 173, 190, 188]

#분석모델 정의
def model(x):
    y = a * x + b
    return y

for x in x_data:
    print('%d에 대한 예측값 : %d' % (x, model(x)))