from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from forum_app.models import Post
from .serializers import PostListCreateSerializer


class PostListCreateView(generics.ListCreateAPIView):
    """API view to list and create posts."""

    queryset = Post.objects.all()
    serializer_class = PostListCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Set the author to the current authenticated user."""

        serializer.save(author=self.request.user)


class PostDetailView(APIView):
    """API view to retrieve, update and delete a post."""

    pass


class CommentListCreateView(APIView):
    """API view to list and create a comment."""

    pass


class CommentDetailView(APIView):
    """API view to retrieve, update and delete a comment."""

    pass