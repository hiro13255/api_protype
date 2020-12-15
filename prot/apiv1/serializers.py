from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Post

class UserSerializer(serializers.ModelSerializer):
    """ユーザーシリアライザー"""
    class Meta:
        model = get_user_model()
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """カテゴリシリアライザ"""
    class Meta:
        model = Category
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    """投稿シリアライザ"""
    class Meta:
        model = Post
        fields = '__all__'