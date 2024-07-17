from rest_framework import serializers
from .models import Player, Problem, Rank
from django.contrib.auth.models import User
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['user_id', 'nickname', 'highscore', 'item', 'gold']
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.highscore = max(validated_data.get('highscore', instance.highscore), instance.highscore)
        instance.item = list(map(int, validated_data.get('item', instance.item).strip('[]').replace(' ', '').split(',')))
        instance.gold = validated_data.get('gold', instance.gold)
        instance.save()
        return instance
class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id','num', 'difficulty']

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ['user_id', 'score']

class UserLoginSerializer(serializers.Serializer):
    userid = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    print("GET IN USERSERIALIZER")
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name']

    def validate(self, data):
        print("valid checking" ,data)
        # 비밀번호와 비밀번호 확인 필드 일치 여부 검사
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password_confirm')  # password_confirm 필드는 user 생성 시 필요 없음
        user = User.objects.create_user(password=password, **validated_data)
        return user