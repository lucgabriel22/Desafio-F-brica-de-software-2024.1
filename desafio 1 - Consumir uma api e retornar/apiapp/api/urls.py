from rest_framework.routers import DefaultRouter
from .viewsets import GithubViewSet
from django.urls import include, path
router = DefaultRouter()

router.register(f'github', GithubViewSet, basename='github')

urlpatterns = [
    path('', include(router.urls)),
]