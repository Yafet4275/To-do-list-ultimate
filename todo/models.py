from django.db import models
#from django.db.models.base import models

class Tarea(models.Model):
    tarea=models.CharField(max_length=100)

    def __str__(self):
        return self.tarea
        