from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from api.serializers import UserSerializer,IssueSerializer
from api.models import Issue
from rest_framework import permissions,authentication
from api.permissions import IsOwner

class SignUpView(CreateAPIView):

    serializer_class = UserSerializer


class IssueListCreateView(ListAPIView,CreateAPIView):

    serializer_class = IssueSerializer

    queryset = Issue.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        serializer.save(owner = self.request.user)


class IssueUpdateDestroyView(UpdateAPIView,DestroyAPIView,RetrieveAPIView):

    serializer_class = IssueSerializer

    queryset = Issue.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]
