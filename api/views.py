from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from articles.models import Article
from .serializers import ArticleSerializer


class ArticleAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer