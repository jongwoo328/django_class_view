from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Article


User = get_user_model()

class ArticleBasicSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='accounts.customuser')
    class Meta:
        model = Article
        fields = '__all__'

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'content',
        )