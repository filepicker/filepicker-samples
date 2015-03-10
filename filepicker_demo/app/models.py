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

    def images_list(self):
        return self.fpfile_url.split(',')

    # Image preview for django admin
    def admin_image(self):
        img = '<img src="{}"/>' * (len(self.images_list()))
        print img
        print self.images_list()
        img = img.format(*self.images_list())
        # print res
        return img
    admin_image.allow_tags = True

    def delete(self, using=None):
        for f in self.images_list():
            try:
                requests.delete(f, params={'key': settings.FILEPICKER_API_KEY})
            except Exception:
                pass
        super(DemoModel, self).delete()


class DemoModelForm(forms.ModelForm):
    class Meta:
        model = DemoModel
        fields = ['text', 'fpfile']
