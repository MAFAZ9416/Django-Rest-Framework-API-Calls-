from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

class BookView(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LaptopView(generics.ListCreateAPIView):

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class LaptopViewById(generics.RetrieveUpdateDestroyAPIView):

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    