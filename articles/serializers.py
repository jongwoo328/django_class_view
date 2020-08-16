from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Article, Comment


User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    article = serializers.PrimaryKeyRelatedField(read_only=True, source='articles.article')
    class Meta:
        model = Comment
        fields = '__all__'
    
    def get_author(self, instance):
        from accounts.serializers import UserBasicSerializer
        return UserBasicSerializer(instance.author).data


class ArticleBasicSerializer(serializers.ModelSerializer):
    # author = serizlizers.UserBasicSerializer(read_only=True)
    # 로 가져올 경우 circular dependency 발생하셔
    # serializers.SerializerMethodField 이용 후
    # get_{field_name} 함수를 정의하여 해결

    author = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
    
    def get_author(self, instance):
        from accounts.serializers import UserBasicSerializer
        return UserBasicSerializer(instance.author).data

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'content',
        )