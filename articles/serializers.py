from rest_framework import serializers

from .models import Article

class ArticleListSerializer(serializers.ListSerializer):
    pass


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'content',
        )
        list_serializer_class = ArticleListSerializer