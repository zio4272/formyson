from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostListSerializer
from rest_framework import permissions
from .permissions import IsUser, IsAdminUser

class PostListCreateAPIView(ListCreateAPIView):

    serializer_class = PostListSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        else:
            self.permission_classes = [IsAdminUser, ]
        return super(PostListCreateAPIView, self).get_permissions()


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Post.objects.all()

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        method = self.request.method
        print(method)
        if method == 'GET':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        else:
            self.permission_classes = [IsAdminUser, ]
        return super(PostDetailAPIView, self).get_permissions()

    def get_queryset(self):
        return self.queryset