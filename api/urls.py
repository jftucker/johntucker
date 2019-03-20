from django.urls import path

from .views import ArticleAPIView, ArticleDetail

urlpatterns = [
    path('<int:pk>/', ArticleDetail.as_view()),
    path('', ArticleAPIView.as_view(), name='API_list'),
]