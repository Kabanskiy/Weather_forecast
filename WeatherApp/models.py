from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30) # наследуем от моделс

    def __str__(self):
        return self.name