from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('사용자 이름은 영숫자 문자만 포함해야 합니다.')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    refresh_token = serializers.CharField(max_length=68, min_length=6, read_only=True)
    access_token = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'refresh_token', 'access_token']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('사용자 정보가 존재하지 않습니다.')

        if not user.is_active:
            raise AuthenticationFailed('활성화 되지 않은 사용자 입니다.')

        if not user.is_verified:
            raise AuthenticationFailed('승인되지 않은 사용자 입니다.')

        return {
            'email': user.email,
            'username': user.username,
            'refresh_token': user.tokens()['refresh'],
            'access_token': user.tokens()['access']
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)