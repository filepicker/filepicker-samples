from django.contrib import admin
from .models import DemoModel


class DemoModelAdmin(admin.ModelAdmin):
    """
    DemoModel Admin class with preview of image from filepicker.io
    """

    readonly_fields = ('fpfile_url', )
    list_display = ('id', 'fpfile', 'fpfile_url', 'admin_image')


admin.site.register(DemoModel, DemoModelAdmin)