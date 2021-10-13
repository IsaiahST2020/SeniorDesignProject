from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Create your views here.
def home_view(request, *args, **kwargs):
	#print(request.user)
	#return HttpResponse("<h1>Hello World</h1>") # string of html code
	return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_condition": True,
		"my_number": 123,
		"my_list": [9, 8, 7, "Six"]
	}
	#return HttpResponse("<h2>Contacts Page</h2>")
	return render(request, "contact.html", my_context)


# Login
def login_view(request, *args, **kwargs):
	if request.method == "POST":
		#form = AuthenticationForm(request=request, data=request.POST)
		#if form.is_valid():
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
		return render(request, "login.html", context={"form":form})


# Register
def register_view(request, *args, **kwargs):
	if request.method == "POST":
		# TO ADD : User Creation
		return redirect('/')
	else:
		form = RegisterForm()
		return render(request, 'register.html', context={"form":form})