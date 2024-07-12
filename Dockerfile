# Dockerfile

# 기본 이미지로 Python 3.12를 사용합니다.
FROM python:3.12

# 환경 변수 설정 (필요에 따라 변경)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# Python 패키지 설치
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 현재 디렉토리의 파일들을 컨테이너의 작업 디렉토리로 복사합니다.
COPY . /app/
