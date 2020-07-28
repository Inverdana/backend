  
from django.contrib import admin
from django.urls import path
from djoser import views
from  rest_framework.routers import DefaultRouter
from .views import EventosViewSet,PostViewSet,ArbolesCatalogoViewSet
router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [ 
    path('inicio/', views.TokenCreateView.as_view()),
    path('salir/', views.TokenDestroyView.as_view()),
    path('yo/', views.UserViewSet.as_view({
        'get': 'me',
    })),
    path('eventos/',EventosViewSet.as_view({
        'get': 'list',
    })),
     path('eventos/<int:pk>/',EventosViewSet.as_view({
        'post': 'inscribirse',
        'delete': 'desinscribirse'
    })),
    path('catalogo/',ArbolesCatalogoViewSet.as_view({
        'get':'list'
    }))
] + router.urls
