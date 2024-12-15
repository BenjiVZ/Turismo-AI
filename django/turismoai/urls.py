"""
URL configuration for turismoai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from turismoai_app.api import (
    RestauranteViewSet,
    AtraccionTuristicaViewSet,
    ActividadAireLibreViewSet,
    CulturaOcioViewSet,
    ComprasViewSet,
    VidaNocturnaViewSet
)

router = routers.DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'atracciones', AtraccionTuristicaViewSet)
router.register(r'actividades', ActividadAireLibreViewSet)
router.register(r'cultura', CulturaOcioViewSet)
router.register(r'compras', ComprasViewSet)
router.register(r'vidanocturna', VidaNocturnaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('turismoai_app.urls')),
]
