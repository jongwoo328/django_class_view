from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ArticleSerializer


class ArticleView(APIView):
    '''
    Article View
    '''
    def post(self, request, format=None):
        article = ArticleSerializer(data=request.data)
        if article.is_valid():
            article.save()
            return Response(article.data, status=status.HTTP_201_CREATED)
        return Response(article.errors, status=status.HTTP_400_BAD_REQUEST)
