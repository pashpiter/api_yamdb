from django.shortcuts import render
from rest_framework import pagination, viewsets, filters

from reviews.models import Genre, Category, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_class =
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_class =
    pagination_class = pagination.PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # permission_class =
    pagination_class = pagination.PageNumberPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category__slug', 'genre_slug', 'name', 'year')