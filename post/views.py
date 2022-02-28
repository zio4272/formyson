from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from comment.models import Comment
from .models import Post
from .serializers import PostBodySerializer, PostSerializer
from rest_framework import permissions
from .permissions import IsUser, IsAdminUser
from rest_framework.response import Response
from django.db.models import Prefetch

class PostListCreateAPIView(ListCreateAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # 메소드별 permission
    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        else:
            self.permission_classes = [IsAdminUser, ] # 커스텀 사용
        return super(PostListCreateAPIView, self).get_permissions()

    # 메소드별 serializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostBodySerializer
        return PostSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Post.objects.all()

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        else:
            self.permission_classes = [IsAdminUser, ]
        return super(PostDetailAPIView, self).get_permissions()

    # 메소드별 serializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        return PostBodySerializer

    def get_queryset(self):
        id = self.kwargs['id']
        post = Post.objects.filter(id=id)
        comments = post.comment_post.all()

        return self.queryset.filter(id=id)