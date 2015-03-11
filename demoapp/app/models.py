from django import forms
from django.db import models


class FileUploaderModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    uploaded_file = models.URLField(blank=False)

    def images_list(self):
        return self.uploaded_file.split(',')

    def uploaded_file_short(self):
        return self.uploaded_file[:50] + '...'


class FileUploaderForm(forms.ModelForm):
    class Meta:
        model = FileUploaderModel
        fields = ['name', 'uploaded_file']
