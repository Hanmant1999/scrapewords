from django.db import models
from  django.db.models import Model

# Create your models here.
class Work (models.Model):
    url=models.CharField(max_length=200,unique=False)
    word=models.TextField(max_length=20000)

def __str__(self):
    return self.url


