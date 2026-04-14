from rest_framework import serializers

from forum_app.models import Comment, Post


class PostListCreateSerializer(serializers.ModelSerializer):
    """Serializer for retrieving, updating and deleting a post."""

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "created_at")
        read_only_fields = ("author", "created_at")


class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer for retrieving, updating an deleting a post."""

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "created_at")
        read_only_fields = ("author", "created_at")


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for listing, creating, retrieving, updating and deleting comments."""

    class Meta:
        model = Comment
        fields = ("id", "post", "text", "author", "created_at")
        read_only_fields = ("author", "created_at")