from django_filters import CharFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, permissions, mixins
from rest_framework.filters import OrderingFilter

from .serializers import *
from .models import *


# VIEWSETS
class LevelViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class CategoryViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    # If we add: mixins.DestroyModelMixin,
    # we also could delete categories
    permission_classes = (permissions.IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class WordViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_fields = ("english_word", "spanish_word", "category",)
    filter_fields = ("english_word", "spanish_word", "category",)
    ordering_fields = ("english_word", "spanish_word", "category",)
    ordering = ("category",)


