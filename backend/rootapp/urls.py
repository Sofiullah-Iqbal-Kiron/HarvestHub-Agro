from django.urls import path
from .api.endpoints import endpoints

urlpatterns = []+endpoints
