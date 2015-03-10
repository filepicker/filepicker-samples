import requests
from django import forms
from django.conf import settings
from django.db import models

from django_filepicker.models import FPFileField


class DemoModel(models.Model):

    text = models.CharField(max_length=255, unique=True)
    fpfile = FPFileField(upload_to='uploads',
                         additional_params={'data-fp-multiple': 'true'})
    fpfile_url = models.URLField(null=True)

    # Image preview for django admin
    def admin_image(self):
        return '<img src="%s"/>' % self.fpfile_url
    admin_image.allow_tags = True

    def delete(self, using=None):
        try:
            requests.delete(self.fpfile_url, params={'key': settings.FILEPICKER_API_KEY})
        except Exception:
            pass
        super(DemoModel, self).delete()


class DemoModelForm(forms.ModelForm):
    class Meta:
        model = DemoModel
        fields = ['text', 'fpfile']
