from rest_framework import serializers
from .models import Comment
from authentication.serializers import UserSerializer
from post.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class CommentBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'comment', 'created_at']