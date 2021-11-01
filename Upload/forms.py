from django import forms

from .models import Upload, FileUpload


class UploadForm(forms.ModelForm):
	class Meta:
		model = FileUpload
		fields = [
			'title',
			'file'
		]
	def clean_title(self, *args, **kwargs):
		cleaned_title = self.cleaned_data.get("title")
		if "CFE" not in cleaned_title:
			return cleaned_title
		else:
			raise forms.ValidationError("this is not a valid title")
	def clean_file_type(self, *args, **kwargs):
		cleaned_data = super(UploadForm, self).clean()
		file = cleaned_data.get('file')

		if ".gcode" not in file:
			raise forms.ValidationError("this is not a gcode file")
		else:
			return file


class RawUploadForm(forms.Form):
    title = forms.CharField(required=True)
    number = forms.CharField(label='')
    date = forms.CharField()
    quantity = forms.IntegerField(initial=1)


class FileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('title', 'file', )
