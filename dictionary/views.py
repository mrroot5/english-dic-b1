from rest_framework import viewsets, permissions, mixins
from .serializers import *
from .models import *


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
    permission_classes = (permissions.IsAdminUser,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer
