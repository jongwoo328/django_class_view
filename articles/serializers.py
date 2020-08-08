from rest_framework import serializers

from .models import Article

class ArticleListSerializer(serializers.ListSerializer):
    pass


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = '__all__'
        list_serializer_class = ArticleListSerializer