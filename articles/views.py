from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from extra_views import CreateWithInlinesView, InlineFormSetFactory, UpdateWithInlinesView
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article, Image
from .forms import ArticleForm, ImageFormSet


class HomePageWithArticles(ListView):
    model = Article
    template_name = 'home.html'
    

class ArticleCreateWithInlinesView(LoginRequiredMixin, CreateWithInlinesView):
    model = Article
    inlines = (ImageFormSet,)
    fields = ('title', 'body', 'post_type',)
    template_name = 'article_new.html'
    login_url = 'login'
    
    def get_success_url(self):
        return self.object.get_absolute_url()

class ArticleUpdateWithInlinesView(LoginRequiredMixin, UpdateWithInlinesView):
    model = Article
    inlines = (ImageFormSet,)
    fields = ('title', 'body', 'post_type',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def get_success_url(self):
        return self.object.get_absolute_url()

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    fields = ('image',)
    template_name = 'article_detail.html'
    login_url = 'login'



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'