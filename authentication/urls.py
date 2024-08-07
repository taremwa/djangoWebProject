from .views import RegistrationView
from django.urls import path


urlpatterns = [
    path('register', RegistrationView.as_view(), name="register")
    path('validate-username', UsernameValidationView.as_view(),
         name="validate-username")
]