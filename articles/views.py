from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .serializers import ArticleSerializer
from .models import Article


class ArticleList(APIView):
    '''
    Article List View
    '''
    @swagger_auto_schema(responses={200: 'OK', 404: 'Not found', 400: 'Bad request'})
    def get(self, request, format=None):
        '''
        Response all artiicles
        '''
        articles = Article.objects.all()
        serializer = ArticleSerializer(instance=articles, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticleSerializer ,responses={201: 'Created', 400: 'Bad request', 400: 'Bad request'})
    def post(self, request, format=None):
        '''
        Create article
        '''
        article = ArticleSerializer(data=request.data)
        if article.is_valid():
            article.save()
            return Response(article.data, status=status.HTTP_201_CREATED)
        return Response(article.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    '''
    Article Detail View
    '''
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    @swagger_auto_schema(responses={200: 'OK', 404: 'Not found', 200: 'OK', 400: 'Bad request'})
    def get(self, request, article_id, format=None):
        article = self.get_object(article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticleSerializer ,responses={200: 'OK', 400: 'Bad request', 404: 'Not found'})
    def put(self, request, article_id, format=None):
        article = self.get_object(article_id)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(responses={204: 'No content (deleted)', 400: 'Bad request'})
    def delete(self, request, article_id, format=None):
        article = self.get_object(article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)