# equal_project/add_data.py

import os
import django

# Django 프로젝트 설정 파일 로드
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'equal_project.settings')
django.setup()

from equal.models import Problem

def add_data(num, difficulty):
    # 예시 데이터 추가
    problem = Problem(num = num, difficulty = 1)

    
    # 데이터베이스에 저장
    problem.save()
    
    print("Data added successfully")

if __name__ == "__main__":
    file_path = 'problems.txt'
    with open(file_path, 'r') as file:
        content = file.read()
    lines = content.replace('\'', '').replace(',','').split(' ')
    for l in lines:
        add_data(l, 1)
