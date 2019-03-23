from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(
        many=True, 
        read_only=True,        
        )

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'body',
            'date',
            'link',
            'post_type',
            'images',
        )