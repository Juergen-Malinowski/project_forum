from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer

class RegistrationView(generics.CreateAPIView):
    """API view for user registration."""

    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]