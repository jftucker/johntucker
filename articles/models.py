from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
    POST_TYPES = (
        ('Job', 'Job'),
        ('Art', 'Art'),
        ('Programming', 'Programming'),
    )

    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=20, choices=POST_TYPES, default='Job')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Image(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='images',
    )
    title = models.CharField(max_length=140, null=True, blank=True)
    image = models.ImageField('image', upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.image.url

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])