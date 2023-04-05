from django.db import models

class registroSafely(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombres')
    area = models.CharField(max_length=50, verbose_name='Área de Trabajo')
    correo = models.EmailField(max_length=50)

class registroSafelyEmpresa(models.Model):
    celular = models.CharField(max_length=20, verbose_name='Celular')
    empresa = models.CharField(max_length=50, verbose_name='Empresa')
    rubro = models.CharField(max_length=50, verbose_name='Rubro')

