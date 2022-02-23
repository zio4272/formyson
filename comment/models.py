from django.db import models

from authentication.models import User
from post.models import Post

class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, related_name='comment_user')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=False, related_name='comment_post')
    comment = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
