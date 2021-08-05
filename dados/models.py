from django.db import models

class Dado(models.Model):
    email = models.EmailField(max_length=200, blank=False, default='')
    cpf = models.IntegerField(blank=False, default='')