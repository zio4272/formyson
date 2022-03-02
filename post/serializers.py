from rest_framework import serializers
from .models import Post, Comment, PostImages

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ['id', 'image']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {
                'id': obj.user.id,
                'username': obj.user.username,
                'email': obj.user.email,
            }

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'created_at', 'updated_at', 'user']

class CommentBodySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['post_id', 'comment']
        examples = {
            'post_id': 1,
            'comment': '댓글입니다' 
        }

class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return {
                'id': obj.user.id,
                'username': obj.user.username,
                'email': obj.user.email,
            }
            
    comments = CommentSerializer(read_only=True, many=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    images = PostImagesSerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user', 'comments', 'comment_count', 'images']

class PostBodySerializer(serializers.ModelSerializer):
    images = serializers.ImageField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'images']
        examples = {
            'title': '제목',
            'content': '내용'
        }
