from django.conf import settings
from django.db import models


class Post(models.Model):
    """Model for forum posts."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the post title."""

        return self.title


class Comment(models.Model):
    """Model for comments on forum posts."""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a short comment preview."""

        return f"Comment by {self.author} on {self.post}"