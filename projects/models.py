from django.db import models

# Create your models here.
class FileUpload(models.Model):
    file = models.FileField(upload_to='myfiles')
