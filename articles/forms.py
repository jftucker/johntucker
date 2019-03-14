from django.forms import ModelForm
from extra_views import InlineFormSet

from .models import Article, Image


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'post_type',)

class ImageForm(ModelForm):
    model = Image
    fields = ('title', 'image',)

class ImageFormSet(InlineFormSet):
    model = Image
    fields = ('title', 'image',)