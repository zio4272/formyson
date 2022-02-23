from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CommentSerializer, CommentBodySerializer, CommentCreateSerializer
from .models import Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticatedOrReadOnly,]
        else:
            self.permission_classes = [IsAuthenticated,]
        return super(CommentListCreateAPIView, self).get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentBodySerializer

    def perform_create(self, serializer):
        print(self.request.user)
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Comment.objects.all()

class CommentDeatilAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            self.permission_classes = [IsAuthenticatedOrReadOnly, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(CommentDeatilAPIView, self).get_permissions()

    # 메소드별 serializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        return CommentBodySerializer

    def get_queryset(self):
        return self.queryset