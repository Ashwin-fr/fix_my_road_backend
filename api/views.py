from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from api.serializers import UserSerializer

class SignUpView(CreateAPIView):

    serializer_class = UserSerializer

    
