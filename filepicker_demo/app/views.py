from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from models import DemoModel, DemoModelForm


def index(request):
    return render_to_response('index.html')


def files_list_view(request):
    """
    List of all uploaded images with preview.
    """
    files = DemoModel.objects.all()
    return render(request, 'list.html', {'files': files})


def file_detailed_view(request, fid):
    """
    File detailed view with ability of simple
    convert (width, height, blur filter)
    """

    try:
        el = DemoModel.objects.get(pk=fid)
    except ObjectDoesNotExist:
        return redirect('list')

    convert_parameters = ''
    if request.method == "POST":
        params = ['w', 'h', 'fit']
        convert = ''
        for i in params:
            if request.POST.get(i):
                convert += '{}={}&'.format(i, request.POST.get(i))
        if request.POST.get('blurAmount'):
            convert += 'filter=blur&blurAmount={}&'.format(request.POST.get('blurAmount'))
        convert_parameters = '/convert?' + convert[:-1] if convert else ''

    return render(request, 'detailed.html',
                  {'file': el, 'convert_parameters': convert_parameters,
                  'form': DemoModelForm()},
                  context_instance=RequestContext(request))


def file_delete_view(request, fid):
    """
    Deleting file from database and
    from filepicker.io, if it's possible
    """

    try:
        f = DemoModel.objects.get(pk=fid)
    except Exception:
        return redirect('list')
    f.delete()

    return redirect('list')


def file_upload_view(request):
    """
    Uploading file, saving it to your local storage and
    also saving filepicker.io url to database
    """

    if request.method == "POST":
        form = DemoModelForm(request.POST, request.FILES)
        if form.is_valid():
            res = form.save()
            res.fpfile_url = request.POST['fpfile']
            res.save()

            return redirect('list')
        else:
            return render(request, "upload.html", {'form': form})
    else:
        form = DemoModelForm()

    return render(request, "upload.html", {'form': form})