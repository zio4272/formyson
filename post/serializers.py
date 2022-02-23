from rest_framework import serializers
from .models import Post
from authentication.serializers import UserSerializer

class PostListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user']
        # read_only_fields = ['user',]
        # depth = 1

# 작성,수정시에는 body에 user 정보 필요없어서 만든 serializer
class PostBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']