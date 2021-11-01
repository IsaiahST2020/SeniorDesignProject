from django.shortcuts import render, redirect

from .forms import UploadForm, RawUploadForm, FileForm

from .models import Upload, FileUpload

# Create your views here.


def upload_detail_view(request):
    # Passing in object from database to HTML
    obj = Upload.objects.get(id=1)
    context = {
        'title': obj.title,
        'quantity': obj.quantity
    }
    return render(request, "upload/detail.html", context)


def upload_create_view(request):
    # Passing in object from database to HTML
    form = UploadForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "upload/upload_create.html", context)

# File Upload View


def file_upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success/')

    else:
        form = FileForm()
    return render(request, 'upload/upload_file.html', context={"form": form})


# Successful File Upload View
def success_view(request, *args, **kwargs):
    return render(request, "upload/success.html", {})


# def upload_create_view(request):
#   my_form = RawUploadForm()
#   if request.method == "POST":
#       my_form = RawUploadForm(request.POST)
#       if my_form.is_valid():
#           # Now the data is good
#           print(my_form.cleaned_data)
#           my_form.save()
#   context = {
#       'form': my_form
#   }
#   return render(request, "upload/upload_create.html", context)
