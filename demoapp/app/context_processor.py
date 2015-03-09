from django.conf import settings


def file_picker_api_key(request):
    return {
        'file_picker_api_key': settings.FILE_PICKER_API_KEY
    }