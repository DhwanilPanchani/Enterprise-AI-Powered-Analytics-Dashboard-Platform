from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    Used for reading user information.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration. Handles password creation securely.
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # The password field is write-only, meaning it's used for input but not shown in output.
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        # Use Django's built-in create_user method to ensure the password is properly hashed.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

