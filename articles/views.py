from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from extra_views import CreateWithInlinesView, InlineFormSetFactory, UpdateWithInlinesView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article, Image
from .forms import ArticleForm, ImageFormSet
from sendmessage.forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


class HomePageWithArticles(ListView):
    model = Article
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_articles'] = self.model.objects.all()
        context['art_articles'] = self.model.objects.filter(post_type='Art')
        context['job_articles'] = self.model.objects.filter(post_type='Job')
        context['programming_articles'] = self.model.objects.filter(post_type='Programming')
        try:
            old_contact_form = self.request.session['contact_form']
        except:
            old_contact_form = None
        context['contact_form'] = ContactForm
        return context

    def post(self, request, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name'] + ' sent a message through hire.johntucker.me!'
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['hire@johntucker.me'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your message was sent!')
            return redirect('home')

class ArticleCreateWithInlinesView(LoginRequiredMixin, CreateWithInlinesView):
    model = Article
    inlines = (ImageFormSet,)
    fields = ('title', 'body', 'link', 'link_text', 'post_type',)
    template_name = 'article_new.html'
    login_url = 'login'
    
    def get_success_url(self):
        return self.object.get_absolute_url()

class ArticleUpdateWithInlinesView(LoginRequiredMixin, UpdateWithInlinesView):
    model = Article
    inlines = (ImageFormSet,)
    fields = ('title', 'body', 'link', 'link_text', 'post_type',)
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