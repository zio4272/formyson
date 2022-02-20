from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post'),
    path('<int:id>', views.PostDetail.as_view(), name='post'),
]