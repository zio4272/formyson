from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostListSerializer
from rest_framework import permissions
from .permissions import IsUser

class PostList(ListCreateAPIView):

    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):

        return serializer.save(user_id=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)

class PostDetail(RetrieveUpdateDestroyAPIView):
    
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsUser,)
    lookup_fields = "id"

    def perform_create(self, serializer):

        return serializer.save(user_id=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)