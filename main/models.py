from django.db import models

# Create your models here.
class file_upload(models.Model):
    file = models.FileField()