from django.shortcuts import render
from rest_framework import viewsets 
from .models import Blog
from .serializers import BlogSerializer
# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    print(66666)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer