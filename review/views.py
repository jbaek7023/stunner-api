from django.shortcuts import render
from rest_framework import generics
from .models import Review
from .serializer import ReviewSerializer

# Create your views here.
class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
