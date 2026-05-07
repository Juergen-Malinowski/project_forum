from rest_framework.throttling import UserRateThrottle


class PostThrottle(UserRateThrottle):
    """Throttle POST requests for post and comment creation."""

    scope = "posts"

    def allow_request(self, request, view):
        """Apply the scoped rate limit only to POST requests."""

        if request.method != "POST":
            return True

        return super().allow_request(request, view)
        