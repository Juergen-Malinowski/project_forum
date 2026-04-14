from rest_framework import serializers

from forum_app.models import Post


class PostListCreateSerializer(serializers.ModelSerializer):
    """Serializer for listing and creating posts."""

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "created_at")
        read_only_fields = ("author", "created_at")