from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apiapp.api import viewsets as githubviewsets
    
route = routers.DefaultRouter()

route.register(f'git', githubviewsets.GithubViewSet, basename='Github')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apiapp.api.urls')),
]

# rotas do autenticador
