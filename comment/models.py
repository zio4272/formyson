from django.db import models

from authentication.models import User
from post.models import Post

class Comment(models.Model):
    comment = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, related_name='comment_user', db_column='user_id')
    post_id = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comment_post', db_column='post_id')

    class Meta:
        db_table = 'comment' # 테이블명 지정
