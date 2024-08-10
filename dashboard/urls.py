from django.urls import path
from .views import dashboard, create_user_profile, profile_success

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('createProfile/', create_user_profile, name='create_user_profile'),
    path('success/', profile_success, name='profile_success'),
]
