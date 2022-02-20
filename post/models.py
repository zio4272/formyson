from django.db import models
from authentication.models import User

class Post(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)