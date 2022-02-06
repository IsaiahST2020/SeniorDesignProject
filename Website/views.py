from .models import Upload, FileUpload
from .forms import UploadForm, RawUploadForm, FileForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.


def home_view(request, *args, **kwargs):
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_condition": True,
        "my_number": 123,
        "my_list": [9, 8, 7, "Six"]
    }
    # return HttpResponse("<h2>Contacts Page</h2>")
    return render(request, "contact.html", my_context)


# Login
def login_view(request, *args, **kwargs):
    if request.method == "POST":
        #form = AuthenticationForm(request=request, data=request.POST)
        # if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        #username = form.cleaned_data.get('username')
        #password = form.cleaned_data.get('password')
        messages.info(request, f"Welcome, {username}")
        return redirect('/')
        # user = authenticate(username=username, password=password)
        # if user is not None:
        # 	if user.is_active:
        # 		login(request, user)
        # 		messages.info(request, f"Welcome, {username}")
        # 		return redirect('/')
    else:
        form = AuthenticationForm()
        return render(request, "login.html", context={"form": form})


# Register
def register_view(request, *args, **kwargs):
    if request.method == "POST":
        # TO ADD : User Creation
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', context={"form": form})


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


@login_required
def file_upload_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # Autofill the upload_by field for the File object
            obj = form.save(commit=False)
            obj.upload_by = request.user
            obj.save()
            return redirect('success/')

    else:
        form = FileForm()
    return render(request, 'upload/upload_file.html', context={"form": form})


# Successful File Upload View
def success_view(request, *args, **kwargs):
    return render(request, "upload/success.html", {})


# Create your views here.
def queue_view(request, *args, **kwargs):
    #queryset = FileUpload.objects.all()
    if request.user.is_staff != True:
        raise Http404()
    queryset = FileUpload.objects.all().order_by('upload_time')
    context = {
        "object_list": queryset
    }
    if request.method == "POST":
        print(request)
    #obj = FileUpload.objects.get(id=1)
    # context = {
    #	'title': obj.title,
    #	'file': obj.file
    # }
    return render(request, "upload/queue.html", context)


def delete_file(request, pk):
    # Ensure priviledged user
    if request.user.is_staff != True:
        raise Http404()
    if request.method == 'POST':
        file = get_object_or_404(FileUpload, pk=pk)
        file.delete()
        return redirect('/queue')
    else:
        raise Http404()


# def upload_create_view(request):
# 	my_form = RawUploadForm()
# 	if request.method == "POST":
# 		my_form = RawUploadForm(request.POST)
# 		if my_form.is_valid():
# 			# Now the data is good
# 			print(my_form.cleaned_data)
# 			my_form.save()
# 	context = {
# 		'form': my_form
# 	}
# 	return render(request, "upload/upload_create.html", context)
