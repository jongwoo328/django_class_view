from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = '__all__'
    
    def get_author(self, instance):
        from accounts.serializers import UserBasicSerializer
        return UserBasicSerializer(instance.author).data


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'image',
        )