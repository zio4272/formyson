from .models import Post, Comment, PostImages
from .serializers import PostBodySerializer, PostImagesSerializer, PostSerializer, CommentSerializer, CommentBodySerializer
from rest_framework import permissions, generics
from .permissions import IsUser, IsAdminUser
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .utils import post_image_s3_upload


class PostListCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        else:
            self.permission_classes = [permissions.IsAdminUser, ]
        return super(PostListCreateAPIView, self).get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostBodySerializer
        return PostSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Post.objects.all()

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
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

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        return PostBodySerializer

    def get_queryset(self):        
        return self.queryset

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentBodySerializer
    permission_classes = [IsUser, ]
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = "id"
    http_method_names = ['post', 'put', 'patch', 'delete']

    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, ]
        return super(CommentDetailView, self).get_permissions()

    def get_queryset(self):
        return self.queryset

class PostImageUploadAPIView(generics.CreateAPIView):
    
    serializer_class = PostImagesSerializer
    parser_classes = [MultiPartParser, ]
    permission_classes = [permissions.IsAdminUser, ]

    def post(self, request, *args, **kwargs):

        image = request.FILES['image']

        upload = post_image_s3_upload(image)
        
        return Response({'img_url': upload.data})