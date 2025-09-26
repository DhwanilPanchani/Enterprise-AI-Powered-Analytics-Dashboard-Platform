# File: backend/user_service/urls.py

from django.contrib import admin
from django.urls import path, include # Make sure to import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line includes all the URLs from your 'users' app under the '/api/' prefix
    path('api/', include('users.urls')),
]