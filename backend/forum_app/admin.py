from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for posts.

    Note:
    'author__username' in search_fields accesses a field of the related
    User model via ForeignKey. Other User fields could also be used.
    """

    list_display = ("id", "title", "author", "created_at")
    search_fields = ("title", "content", "author__username")
    list_filter = ("created_at", "author")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin configuration for comments."""

    list_display = ("id", "post", "author", "created_at")
    search_fields = ("text", "author__username", "post__title")
    list_filter = ("created_at", "author")
