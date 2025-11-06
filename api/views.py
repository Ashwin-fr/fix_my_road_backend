from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from api.serializers import UserSerializer,IssueSerializer
from api.models import Issue,StillPresent
from rest_framework import permissions,authentication
from api.permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SignUpView(CreateAPIView):

    serializer_class = UserSerializer


class IssueListCreateView(ListAPIView,CreateAPIView):

    serializer_class = IssueSerializer

    queryset = Issue.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        serializer.save(owner = self.request.user)

    def get_serializer_context(self):
        
        context = super().get_serializer_context()

        context['user'] = self.request.user.id

        return context


class IssueUpdateDestroyView(UpdateAPIView,DestroyAPIView,RetrieveAPIView):

    serializer_class = IssueSerializer

    queryset = Issue.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]


class StillPresentView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        id = kwargs.get('pk')

        # issue_object = Issue.objects.get(id = id)

        issue_object = get_object_or_404(Issue,id = id)

        if StillPresent.objects.filter(owner = request.user,issue = issue_object).exists():

            return Response({'message':'User already reacted'},status=status.HTTP_406_NOT_ACCEPTABLE)

        StillPresent.objects.create(owner = request.user,issue = issue_object)

        return Response({'message':'Ok'},status=status.HTTP_201_CREATED)




