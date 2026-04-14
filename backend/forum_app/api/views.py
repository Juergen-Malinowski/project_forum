from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from forum_app.models import Comment, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, PostDetailSerializer, PostListCreateSerializer


class PostListCreateView(generics.ListCreateAPIView):
    """API view to list and create posts."""

    queryset = Post.objects.all()
    serializer_class = PostListCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Set the author to the current authenticated user."""

        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update and delete a post."""

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    """API view to list and create a comment."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Set the author to the current authenticated user."""

        serializer.save(author=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update and delete a comment."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]