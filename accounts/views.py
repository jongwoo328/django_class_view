from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .serializers import UserCreateSerializer, UserBasicSerializer, UserArticleSerializer


User = get_user_model()

class UserList(APIView):
    @swagger_auto_schema(responses={200: 'OK', 400: 'Bad request', 404: 'Not found', 500: 'Internal server error'})
    def get(self, request):
        users = User.objects.all()
        serializer = UserBasicSerializer(instance=users, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=UserCreateSerializer, responses={201: 'Created', 400: 'Bad request', 500: 'Internal server error'})
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            return Response(UserBasicSerializer(instance=user).data, status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    def get_object(self, user_id):
        return get_object_or_404(User, pk=user_id)
    
    @swagger_auto_schema(responses={200: 'OK', 400: 'Bad request', 404: 'Not found', 500: 'Internal server error'})
    def get(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserBasicSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=UserCreateSerializer, responses={200: 'OK', 400: 'Bad request', 404: 'Not found', 500: 'Internal server error'})
    def put(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserCreateSerializer(instance=user)
        user = serializer.update(user, request.data)
        return Response(UserBasicSerializer(user).data, status=status.HTTP_200_OK)
    
    def delete(self, request, user_id):
        user = self.get_object(user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserArticle(APIView):
    def get_object(self, user_id):
        return get_object_or_404(User, pk=user_id)
    
    def get(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserArticleSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)