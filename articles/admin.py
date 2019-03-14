from django.contrib import admin

from .models import Article, Image


class ImagesInline(admin.TabularInline):
    model = Image
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Image)