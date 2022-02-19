from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    # 상세화면에 보여줄 필드 설정 없는경우 전체 보여줌
    # fields = ['username']
    # 목록에 보여줄 데이터
    list_display = ('username', 'email') 
    

admin.site.register(User, UserAdmin)