from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user') 
    

admin.site.register(Post, PostAdmin)