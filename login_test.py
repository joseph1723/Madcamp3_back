from django.contrib.auth import authenticate
# from equal.models import Player  # 예시 모델 임포트

user_id = 'myuserid'
password = 'mypassword'

user = authenticate(user_id=user_id, password=password)

if user is not None:
    print("success")
    # 인증 성공
    # 로그인 로직 등을 수행할 수 있음
else:
    print("fail")
    # 인증 실패
    # 사용자에게 알맞은 오류 처리를 수행할 수 있음
