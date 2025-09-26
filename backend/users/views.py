# File: backend/users/views.py

from rest_framework import generics, response, status
from .serializers import RegisterSerializer, UserSerializer

# New imports for the protected view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class RegisterAPI(generics.GenericAPIView):
    """
    API view for user registration.
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return response.Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        }, status=status.HTTP_201_CREATED)


# --- Add this new class ---
class DashboardAPI(APIView):
    """
    A protected view that only authenticated users can access.
    """
    # This line ensures that a user must provide a valid token to access this view
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handles GET request and returns a secret message if the user is authenticated.
        """
        user = request.user
        message = f"Welcome to the secret dashboard, {user.username}! Your data is safe here."
        return response.Response({"message": message}, status=status.HTTP_200_OK)