"""PrinterSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pages import views
from Upload.views import upload_detail_view, upload_create_view, file_upload_view, success_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    path('contact/', views.contact_view, name="contacts"),
    path('upload/', file_upload_view, name="File Upload"),
    path('create/', upload_create_view, name="Create Upload"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('upload/success/', success_view, name="success")
]
