from django.urls import path

from .views import RegisterAccount

# accounts/register/
#         /login/
#         /delete/

endpoints = [
    path('accounts/register/', RegisterAccount.as_view(), name='register-account'),
]
