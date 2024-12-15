from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurante(models.Model):
    nombre = models.CharField(max_length=200)
    tipo_cocina = models.CharField(max_length=100)
    direccion = models.TextField()
    horario = models.TextField()
    opiniones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class AtraccionTuristica(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    horario = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    opiniones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class ActividadAireLibre(models.Model):
    NIVELES_DIFICULTAD = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
        ('experto', 'Experto'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    horario = models.TextField()
    equipo_necesario = models.TextField()
    nivel_dificultad = models.CharField(max_length=20, choices=NIVELES_DIFICULTAD)
    opiniones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class CulturaOcio(models.Model):
    TIPOS = [
        ('museo', 'Museo'),
        ('teatro', 'Teatro'),
        ('galeria', 'Galería'),
        ('centro_cultural', 'Centro Cultural'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField()
    horario = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    opiniones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Compras(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    horario = models.TextField()
    productos = models.TextField()
    opiniones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class VidaNocturna(models.Model):
    TIPOS = [
        ('bar', 'Bar'),
        ('club', 'Club'),
        ('discoteca', 'Discoteca'),
        ('pub', 'Pub'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    direccion = models.TextField()
    horario = models.TextField()
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    opiniones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre