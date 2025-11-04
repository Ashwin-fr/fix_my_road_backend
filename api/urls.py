from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('auth/register/',views.SignUpView.as_view()),
    path('auth/login/',ObtainAuthToken.as_view()),
]