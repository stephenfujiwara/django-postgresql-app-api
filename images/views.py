from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from rest_framework.permissions import IsAuthenticated

from .remove_bg import remove_bg

class ImageView(APIView):
    def post(self, request):
        if 'file' in request.data:
            file = request.data['file']
            output_img = remove_bg(file)
            img_model = Image()
            img_model.img.save(file.name, output_img)
            serializer = ImageSerializer(img_model)
            return Response(serializer.data)
        return Response({"error": "file was not received"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    
class ImageViewDetail(APIView):

    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response({"error: Could not find image in database"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        image = self.get_object(pk=pk)
        img = image.img.file 
        return HttpResponse(FileWrapper(img), content_type="image/png")

class UserImagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        images = user.image_set.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if 'file' in request.data:
            file = request.data['file']
            output_img = remove_bg(file)
            img_model = Image(author=request.user)
            img_model.img.save(file.name, output_img)
            serializer = ImageSerializer(img_model)
            return Response(serializer.data)
        return Response({"error": "file was not received"}, status=status.HTTP_400_BAD_REQUEST)
    
class UserImagesViewDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response({"error: Could not find image in database"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        image = self.get_object(pk=pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







