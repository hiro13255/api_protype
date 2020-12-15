from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import Post, Category
from .serializers import CategorySerializer, PostSerializer

class CategoryListAPIView(generics.ListAPIView):
    """カテゴリモデルの取得APIクラス"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListAPIView(generics.ListAPIView):
    """投稿モデルの取得APIクラス"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer