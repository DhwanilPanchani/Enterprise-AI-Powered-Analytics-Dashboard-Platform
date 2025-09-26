# File: backend/users/urls.py

from django.urls import path
from .views import RegisterAPI, DashboardAPI # Import the new DashboardAPI

# Import the pre-built views from the Simple JWT library
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Registration endpoint
    path('register/', RegisterAPI.as_view(), name='register'),
    
    # Login endpoint (returns access and refresh tokens)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Token refresh endpoint
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Protected dashboard endpoint
    path('dashboard/', DashboardAPI.as_view(), name='dashboard'),
]