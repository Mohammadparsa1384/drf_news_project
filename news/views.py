from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from accounts.models import CustomUser
from .models import News
from .serializers import NewsSerializer
from accounts.serializers import CustomUserSerializer
# Create your views here.

class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

class AuthorViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()