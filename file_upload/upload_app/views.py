from django.http import HttpResponse
from django.shortcuts import render
from upload_app.forms import FileUploadForm
from upload_app.models import FileSimpleModel


def upload_file(request):
    """
    文件接收 view
    :param request: 请求
    :return:
    """
    if request.method == 'POST':
        my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            # f = my_form.cleaned_data['my_file']
            # handle_uploaded_file(f)
            file_model = FileSimpleModel()
            file_model.file_field = my_form.cleaned_data['my_file']
            file_model.save()
        return HttpResponse('Upload Success')
    else:
        my_form = FileUploadForm()
    return render(request, 'upload_temp.html', {'form': my_form})


def search_file(request):
    import os
    return HttpResponse(os.popen('dir').read())