from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    UpdateAPIView
from rest_framework.response import Response

from books.models import (Book, Employee, Reader, Kartoteka)
from .serializers import BookSerializer, ReaderSerializer, KartotekaSerializer


class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReaderApiView(ListCreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class KartotekaListView(ListAPIView):
    queryset = Kartoteka.objects.all()
    serializer_class = KartotekaSerializer


class KartotekaDetailView(RetrieveAPIView):
    queryset = Kartoteka.objects.filter()
    serializer_class = KartotekaSerializer
    # lookup_field = 'reader__first_name'


class KartotekaUpdateView(UpdateAPIView):
    queryset = Kartoteka.objects.all()
    serializer_class = KartotekaSerializer
