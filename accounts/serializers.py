from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from articles.models import Article
from articles.serializers import ArticleBasicSerializer


User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwagrs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, data):
        user = User(
            email=data['email'],
            username=data['username']
        )
        user.set_password(data['password'])
        user.save()
        return user

    def update(self, user, data):
        user = get_object_or_404(User, pk=user.id)

        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)

        if email:
            user.email = email
        if username:
            user.username = username
        if password:
            user.set_password(password)
        user.save()
        return user
            


class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class UserArticleSerializer(UserBasicSerializer):
    articles = ArticleBasicSerializer(many=True, read_only=True)
    
    class Meta(UserBasicSerializer.Meta):
        fields = UserBasicSerializer.Meta.fields + ('articles',)