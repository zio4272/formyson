from django.db import models
from authentication.models import User

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, related_name='post_user')
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'

class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, related_name='comment_user')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name='comments', db_column='post_id')
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'