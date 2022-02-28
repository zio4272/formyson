from rest_framework import serializers
from .models import Post
from authentication.serializers import UserSerializer
from comment.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user']

# 작성,수정시에는 body에 user 정보 필요없어서 만든 serializer
class PostBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        examples = {
            'title': '제목',
            'content': '내용'
        }