from django.shortcuts import get_object_or_404
from django.http import FileResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.renderers import MultiPartRenderer

from drf_yasg.utils import swagger_auto_schema

from .serializers import ImageUploadSerializer, ImageSerializer
from .models import Image


class ImageView(APIView):

    # 일반적으로 HTML form data를 완벽하게 지원하기 위해 FormParser와 MultiPartParser를 함께 사용.
    parser_classes = (FormParser, MultiPartParser, )

    @swagger_auto_schema(request_body=ImageUploadSerializer, responses={201: 'Created', 400: 'Bad request', 401: 'Unauthorized', 500: 'Internal server error'})
    def post(self, request, format=None):
        serializer = ImageUploadSerializer(data=request.FILES)
        if serializer.is_valid():
            serializer.save(
                author=request.user,
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ImageDetail(APIView):
    
    parser_classes = (FormParser, MultiPartParser, )

    def get_object(self, image_id):
        return get_object_or_404(Image, pk=image_id)

    @swagger_auto_schema(responses={200: 'OK', 400: 'Bad Request', 401: 'Unauthorized', 500: 'Internal server error'})
    def get(self, request, image_id, format=None):
        image = self.get_object(image_id)
        return Response(ImageSerializer(instance=image).data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=ImageUploadSerializer, responses={200: 'OK', 400: 'Bad request', 401: 'Unauthorized', 500: 'Internal server error'})
    def put(self, request, image_id, format=None):
        image = self.get_object(image_id)
        serializer = ImageUploadSerializer(instance=image, data=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(responses={204: 'Deleted', 400: 'Bad request', 500: 'Internal server error'})
    def delete(self, request, image_id, format=None):
        image = self.get_object(image_id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        