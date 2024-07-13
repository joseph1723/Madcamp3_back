from django.urls import path
from .views import PlayerListCreate, ProblemListCreate, PlayerDetailUpdate, RankListCreateAPIView, PlayerReturn, UserLoginAPIView, UserSignUpAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/players/', PlayerListCreate.as_view(), name='player-list-create'),
    path('api/players/<str:user_id>/update', PlayerDetailUpdate.as_view(), name='player-detail-update'),
    path('api/players/<str:user_id>/', PlayerReturn.as_view(), name = 'player-return'),
    path('api/problems/', ProblemListCreate.as_view(), name='problem-list-create'),
    path('api/ranks/', RankListCreateAPIView.as_view(), name='rank-list-create'),
    path('api/login/', UserLoginAPIView.as_view(), name = 'api-login'),
    path('api/signup/', UserSignUpAPIView.as_view(), name='api-signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
