from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .serializers import ArticleBasicSerializer, ArticleCreateSerializer, CommentSerializer
from .models import Article, Comment


class ArticleList(APIView):
    '''
    Article List View
    '''
    @swagger_auto_schema(responses={200: 'OK', 404: 'Not found', 400: 'Bad request', 500: 'Internal server error'})
    def get(self, request, format=None):
        '''
        Response all artiicles
        '''
        articles = Article.objects.all()
        serializer = ArticleBasicSerializer(instance=articles, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticleCreateSerializer ,responses={201: 'Created', 400: 'Bad request', 400: 'Bad request', 500: 'Internal server error'})
    def post(self, request, format=None):
        '''
        Create article
        '''
        article = ArticleCreateSerializer(data=request.data)
        if article.is_valid(raise_exception=True):
            article.save(author=request.user)
            return Response(article.data, status=status.HTTP_201_CREATED)


class ArticleDetail(APIView):
    '''
    Article Detail View
    '''
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    @swagger_auto_schema(responses={200: 'OK', 404: 'Not found', 200: 'OK', 400: 'Bad request', 500: 'Internal server error'})
    def get(self, request, article_id, format=None):
        article = self.get_object(article_id)
        serializer = ArticleBasicSerializer(article)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticleCreateSerializer ,responses={200: 'OK', 400: 'Bad request', 404: 'Not found', 500: 'Internal server error'})
    def put(self, request, article_id, format=None):
        article = self.get_object(article_id)
        serializer = ArticleCreateSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(responses={204: 'No content (deleted)', 400: 'Bad request', 500: 'Internal server error'})
    def delete(self, request, article_id, format=None):
        article = self.get_object(article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentCreate(APIView):
    @swagger_auto_schema(request_body=CommentSerializer, responses={201: 'Created', 400: 'Bad request', 500: 'Internal server error'})
    def post(self, request, article_id, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save(
                author=request.user,
                article=get_object_or_404(Article, pk=article_id)
            )
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)


class CommentDetail(APIView):
    def get_object(self, comment_id):
        return get_object_or_404(Comment, pk=comment_id)

    @swagger_auto_schema(request_body=CommentSerializer, responses={200: 'OK', 400: 'Bad request', 500: 'Internal server error'})
    def put(self, request, article_id, comment_id, format=None):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(responses={204: 'Deleted', 400: 'Bad Request', 500: 'Internal server error'})
    def delete(self, request, article_id, comment_id, format=None):
        comment = self.get_object(comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)