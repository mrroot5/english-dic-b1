from django_filters import CharFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, permissions, mixins
from rest_framework.filters import OrderingFilter

from .serializers import *
from .models import *


# FILTERS
class WordFilter(FilterSet):
    english_word_contains = CharFilter(field_name="english_word", lookup_expr='contains')
    spanish_word_contains = CharFilter(field_name="spanish_word", lookup_expr='contains')

    class Meta:
        model = Word
        fields = ["english_word_contains", "spanish_word_contains", "category"]


# VIWSETS
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
    filter_class = WordFilter
    ordering_fields = ("english_word", "spanish_word", "category",)
    ordering = ("category",)


