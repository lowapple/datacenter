FROM ubuntu:16.04

MAINTAINER DayTour <lowapple99@gmail.com>


ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

# 기본 패키지 설치
RUN apt-get update
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-setuptools python3-wheel gcc
RUN apt-get install -y git
RUN apt-get install -y python3-pip
RUN apt-get install -y mysql

# pip 업그레이드
RUN pip3 install --upgrade pip

# 디렉토리 생성 & 파일 이동
ADD . /tourcenter

# 5000번 포트 개방
EXPOSE 5000

# 작업 디렉토리 이동
WORKDIR /tourcenter

# 작업 디렉토리에 있는 requirements.txt로 패키지 설치
RUN pip3 install -r requirements.txt

# 컨테이너에서 실행될 명령어. 컨테이거나 실행되면 app.py를 실행시킨다.
CMD python3 app.py
