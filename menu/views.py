from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializer import MenuSerializer

# Create your views here.
class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
