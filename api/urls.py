from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

# app_name = "api"
urlpatterns = [
    path('auth/', include('auth_client.urls')),
]
