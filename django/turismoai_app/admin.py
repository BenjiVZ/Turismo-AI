from django.contrib import admin
from .models import (
    Restaurante, 
    AtraccionTuristica, 
    ActividadAireLibre,
    CulturaOcio,
    Compras,
    VidaNocturna
)

admin.site.register(Restaurante)
admin.site.register(AtraccionTuristica)
admin.site.register(ActividadAireLibre)
admin.site.register(CulturaOcio)
admin.site.register(Compras)
admin.site.register(VidaNocturna)