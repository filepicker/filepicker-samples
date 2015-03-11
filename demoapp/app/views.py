import requests

from django.template import RequestContext
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from models import FileUploaderModel, FileUploaderForm


def index(request):
    return render(request, 'index.html')


def save_image(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        uploaded_file = request.POST.get('uploaded_file', None)
        if not name or not uploaded_file:
            pass
        else:
            form = FileUploaderForm(request.POST)
            if form.is_valid():
                form.save()

        return redirect('images_list')

    return render(request, 'upload.html', context_instance=RequestContext(request))


def images_list(request):
    files = FileUploaderModel.objects.all()
    return render(request, 'list.html', {'files': files})


def image_view(request, fid):
    try:
        el = FileUploaderModel.objects.get(pk=fid)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist

    if request.method == "POST":
        params = ['w', 'h', 'fit']
        convert = ''
        for i in params:
            if request.POST.get(i):
                convert += '{}={}&'.format(i, request.POST.get(i))
        if request.POST.get('blurAmount'):
            convert += 'filter=blur&blurAmount={}&'.format(request.POST.get('blurAmount'))
        convert_parameters = '/convert?' + convert[:-1] if convert else ''
    else:
        convert_parameters = ''

    return render(request, 'detailed.html', {'file': el,
                                             'convert_parameters': convert_parameters})


def image_delete(request, fid):
    try:
        f = FileUploaderModel.objects.get(pk=fid)
    except ObjectDoesNotExist:
        return redirect('images_list')

    url = f.uploaded_file
    for i in url.split(','):
        try:
            requests.delete(i, params={'key': settings.FILE_PICKER_API_KEY})
        except Exception:
            pass
    f.delete()

    return redirect('images_list')