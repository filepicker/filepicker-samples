from django.db import models


class FileUploaderModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    uploaded_file = models.URLField(blank=False)