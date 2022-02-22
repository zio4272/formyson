from rest_framework import serializers
from .models import Post
from authentication.serializers import UserSerializer

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user']
        depth = 1