from rest_framework import serializers
from . models import Category, News
from accounts.models import CustomUser

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id",'title']
        

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name="author-detail",
        queryset= CustomUser.objects.all()
    )
    category = CategorySerializer(many=True)
    class Meta:
        model = News 
        fields = ["id","title","author","category","body"]