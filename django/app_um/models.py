from django.db import models

class Rastreio(models.Model):
    session_id = models.CharField(max_length=255, null=True )
    ip = models.GenericIPAddressField(null=True )
    pais = models.CharField(max_length=255, null=True )
    estado = models.CharField(max_length=255, null=True )
    cidade = models.CharField(max_length=255, null=True )
    referer = models.TextField(null=True )
    url = models.TextField(null=True )
    device = models.CharField(max_length=255, null=True )
    date_added = models.DateTimeField()

