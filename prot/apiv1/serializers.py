from rest_framework import seriarizers
from django.contrib.auth import get_user_model
from .models import Category,Post

"""ユーザー用シリアライザ"""
class UserSerialiser(seriarizers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

"""カテゴリー用紙リアライザー"""
class CategorySerializer(seriarizers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

"""投稿用シリアライザー"""
class PostSerializer(seriarizers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
