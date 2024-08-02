from .views import RegistrationView
from django.urls import path


urlpatters = [
    path('register', RegistrationView.as_view(), name="register")
]