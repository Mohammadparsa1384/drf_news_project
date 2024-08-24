from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

# class UserListView(generics.ListCreateAPIView):
#     serializer_class = CustomUserSerializer
#     queryset  = CustomUser.objects.all()

# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CustomUserSerializer
#     queryset = CustomUser.objects.all()
