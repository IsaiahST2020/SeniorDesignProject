from django.db import models

# Create your models here.
class Upload(models.Model):
	title = models.CharField(max_length=120)
	number = models.TextField(blank=True)
	date = models.TextField(blank=True, null=True)
	quantity = models.IntegerField(default=1)


class FileUpload(models.Model):
	title = models.CharField(max_length=64)
	#when_uploaded = models.DateTimeField(auto_now_add=True)
	file = models.FileField(upload_to="uploads/")

