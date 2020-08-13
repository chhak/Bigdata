"""
날짜 : 2020/07/22
이름 : 김철학
내용 : 파이썬 Hadoop 실습하기
"""
from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop
import webhdfspy

hdfs = webhdfspy.WebHDFSClient('192.168.100.101', 50070, 'root')
#print(hdfs.listdir('/'))

#hdfs.mkdir('/test1')
hdfs.copyfromlocal(local_path='/home/bigdata/naver', hdfs_path='/naver', overwrite=True)

print('완료')
#Hadoop 접속
#Local의 /home/bigdata/naver/naver-20-xx-xx를 하둡 /naver/ 복사
#Local의 /home/bigdata/naver/naver-20-xx-xx를 삭제
#프로그램 종료


