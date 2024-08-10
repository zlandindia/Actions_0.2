from django.urls import path
from .views import suggesions


urlpatterns = [
    path('', suggesions)
]

