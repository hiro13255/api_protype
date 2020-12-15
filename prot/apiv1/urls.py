from django.urls import path
from . import views

app_name = 'apiv1'
urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view()),
    path('posts/', views.PostListAPIView.as_view()),
]