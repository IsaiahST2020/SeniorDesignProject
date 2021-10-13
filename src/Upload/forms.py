from django import forms

from .models import Upload, FileUpload

class UploadForm(forms.ModelForm):
	class Meta:
		model = Upload
		fields = [
			'title',
			'quantity'
		]
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if "CFE" in title:
			return clean_title
		else:
			raise forms.ValidationError("this is not a valid title")


class RawUploadForm(forms.Form):
	title = forms.CharField(required=True)
	number = forms.CharField(label='')
	date = forms.CharField()
	quantity = forms.IntegerField(initial=1)


class FileForm(forms.ModelForm):
	class Meta:
		model = FileUpload
		fields = ('title', 'file', )