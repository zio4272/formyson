from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListCreateAPIView.as_view(), name='post'),
    path('<int:id>', views.PostDetailAPIView.as_view(), name='post_detail'),
    path('comment', views.CommentCreateAPIView.as_view(), name='comment'),
    path('comment/<int:id>', views.CommentDetailView.as_view(), name='comment_detail'),
]