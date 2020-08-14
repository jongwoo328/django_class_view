from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ArticleSerializer
from .models import Article


class ArticleList(APIView):
    '''
    Article List View
    '''
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(instance=articles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
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

    def get(self, request, article_id, format=None):
        article = self.get_object(article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, article_id, format=None):
        article = self.get_object(article_id)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, article_id, format=None):
        article = self.get_object(article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
