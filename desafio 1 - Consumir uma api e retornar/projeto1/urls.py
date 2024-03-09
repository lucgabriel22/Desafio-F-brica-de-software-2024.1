from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from apiapp.api import viewsets as githubviewsets
    
route = routers.DefaultRouter()

route.register(f'git', githubviewsets.GithubViewSet, basename='Github')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apiapp.api.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls)
]

# rotas do autenticador
