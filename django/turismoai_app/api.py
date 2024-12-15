from rest_framework import viewsets
from .models import (
    Restaurante, 
    AtraccionTuristica, 
    ActividadAireLibre,
    CulturaOcio,
    Compras,
    VidaNocturna
)
from .serializers import (
    RestauranteSerializer,
    AtraccionTuristicaSerializer,
    ActividadAireLibreSerializer,
    CulturaOcioSerializer,
    ComprasSerializer,
    VidaNocturnaSerializer
)

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class AtraccionTuristicaViewSet(viewsets.ModelViewSet):
    queryset = AtraccionTuristica.objects.all()
    serializer_class = AtraccionTuristicaSerializer

class ActividadAireLibreViewSet(viewsets.ModelViewSet):
    queryset = ActividadAireLibre.objects.all()
    serializer_class = ActividadAireLibreSerializer

class CulturaOcioViewSet(viewsets.ModelViewSet):
    queryset = CulturaOcio.objects.all()
    serializer_class = CulturaOcioSerializer

class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer

class VidaNocturnaViewSet(viewsets.ModelViewSet):
    queryset = VidaNocturna.objects.all()
    serializer_class = VidaNocturnaSerializer 