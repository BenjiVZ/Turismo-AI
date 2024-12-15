from rest_framework import serializers
from .models import (
    Restaurante, 
    AtraccionTuristica, 
    ActividadAireLibre,
    CulturaOcio,
    Compras,
    VidaNocturna
)

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class AtraccionTuristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtraccionTuristica
        fields = '__all__'

class ActividadAireLibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadAireLibre
        fields = '__all__'

class CulturaOcioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturaOcio
        fields = '__all__'

class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = '__all__'

class VidaNocturnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VidaNocturna
        fields = '__all__' 