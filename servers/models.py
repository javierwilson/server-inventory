from django.db import models


class Server(models.Model):
    country = models.CharField(max_length=2)
    dn_id = models.CharField(max_length=16)
    machine_id = models.IntegerField()
    created = models.DateTimeField('date created')
