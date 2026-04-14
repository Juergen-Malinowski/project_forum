from django.contrib.auth.models import User

from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""

    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "repeated_password")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, value):
        """Validate that the email address is unique."""

        value = value.lower()

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )
        return value

    def validate_username(self, value):
        """Validate that the username is unique."""

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "A user with this username already exists."
            )
        return value

    def validate(self, attrs):
        """Validate that both password fields match."""

        if attrs["password"] != attrs["repeated_password"]:
            raise serializers.ValidationError(
                {"password": "Passwords do not match."}
            )
        return attrs

    def create(self, validated_data):
        """
        Create and return a new user.

        Important: store the email address in lowercase.
        """

        validated_data["email"] = validated_data["email"].lower()
        validated_data.pop("repeated_password")
        return User.objects.create_user(**validated_data)