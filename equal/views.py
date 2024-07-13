from django.shortcuts import render
from rest_framework import generics
from .models import Player, Problem, Rank
from django.contrib.auth.models import User
from .serializers import PlayerSerializer, ProblemSerializer, RankSerializer, UserLoginSerializer, UserSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated

class PlayerListCreate(generics.ListCreateAPIView):
    players = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all()

class PlayerDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'user_id'

class PlayerReturn(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'user_id'


class ProblemListCreate(generics.ListCreateAPIView):
    problems = Problem.objects.all()
    serializer_class = ProblemSerializer

    permission_classes = [IsAuthenticated]  # 인증이 필요한 뷰 설정
    def get_queryset(self):
        return Problem.objects.all()

class RankListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rank.objects.order_by('-score')  # score 내림차순 정렬
    serializer_class = RankSerializer
    permission_classes = [IsAuthenticated]  # 인증이 필요한 뷰 설정

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        new_score = int(request.data.get('score'))

        existing_rank = Rank.objects.filter(user_id=user_id).first()

        if existing_rank:
            existing_rank.update_score_if_higher(new_score)
            return Response(self.get_serializer(existing_rank).data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    # queryset = Rank.objects.order_by('-score')  # score 내림차순 정렬
    # serializer_class = RankSerializer 
    # def post(self, request, *args, **kwargs):
    #     user_id = request.data.get('user_id')
    #     new_score = int(request.data.get('score'))

    #     existing_rank = Rank.objects.filter(user_id=user_id).first()

    #     if existing_rank:
    #         existing_rank.update_score_if_higher(new_score)
    #         return Response(self.get_serializer(existing_rank).data, status=status.HTTP_200_OK)
    #     else:
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginAPIView(APIView):
    print("LOGIN CALLED")
    def get(self, request):
        print("LOGINEDWW")
        # Return something for GET requests (e.g., login form)
        return Response({'message': 'Please login'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            userid = serializer.validated_data['userid']
            password = serializer.validated_data['password']
            user = authenticate(request, username=userid, password=password)
            if user is not None:
                login(request, user)
                print("Login completed")
                return Response({'user_id': userid}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserSignUpAPIView(APIView):
    def post(self, request):
        print("Signup Gotin")
        print(request.data)
        serializer = UserSerializer(data=request.data)
        print("CHECKING!")
        if serializer.is_valid():
            
            # 사용자 생성
            print("for_chec")
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                email=serializer.validated_data['email'],
                first_name=serializer.validated_data.get('first_name', ''),
                last_name=serializer.validated_data.get('last_name', ''),
            )
            player_data = {'user_id': request.data['username'], 'nickname' : request.data['nickname'], 'email' : request.data['email']}  # user_id는 User 모델의 기본 키
            player_serializer = PlayerSerializer(data=player_data)
            if player_serializer.is_valid():
                print("check")
                player_serializer.save()
            else:
                # Player 생성에 실패한 경우, 사용자도 삭제할 수 있음
                user.delete()
                return Response(player_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
            return Response({'user_id': user.username}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['POST'])
# def login(request):
#     if request.method == 'POST':
#         user_id = request.data.get('userid')
#         password = request.data.get('password')

#         # 사용자 인증
#         user = authenticate(request, userid=user_id, password=password)

#         if user is not None:
#             # 인증 성공
#             return JsonResponse({'message': 'Login successful', 'user_id': user.user_id})
#         else:
#             # 인증 실패
#             return JsonResponse({'message': 'Login failed'}, status=400)

# Create your views here.
