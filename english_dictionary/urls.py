from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.views.generic import RedirectView
from dictionary.views import WordViewSet, LevelViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'word', WordViewSet)
router.register(r'level', LevelViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='admin/')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include(router.urls), name='api'),
]
