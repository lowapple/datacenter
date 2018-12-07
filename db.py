# DB와 관련된 모듈/클래스를 정의 합니다.
# DB접속과 관련된 데이터는 config에 정의 합니다.

import pymysql
import config

# MySQL Connection 연결
conn = config.connectMySQL()
curs = conn.cursor()