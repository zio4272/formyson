from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentListCreateAPIView.as_view(), name='comment'),
    path('<int:id>', views.CommentDeatilAPIView.as_view(), name='comment_detail'),
]