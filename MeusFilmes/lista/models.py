from django.db import models

# Create your models here.

class Filme(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    ano = models.CharField(max_length=4)
    visto = models.BooleanField(default=False)

    def __str__(self):
        return self.title