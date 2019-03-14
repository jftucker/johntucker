from django.urls import path

from .views import (
    HomePageWithArticles,
    ArticleListView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateWithInlinesView,
    ArticleUpdateWithInlinesView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateWithInlinesView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateWithInlinesView.as_view(), name='article_new'),
    path('list/', ArticleListView.as_view(), name='article_list'),
    path('', HomePageWithArticles.as_view(), name='home'),
]