from rest_framework import serializers

from post.models import Post
from .models import Comment
from authentication.serializers import UserSerializer
from post.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class CommentBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment', 'created_at']
        examples = {
            'comment': '내용',
        }

class CommentCreateSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Comment
        fields = ['id','post_id', 'comment', 'created_at']
        examples = {
            'post_id': 1,
            'comment': '내용',
        }