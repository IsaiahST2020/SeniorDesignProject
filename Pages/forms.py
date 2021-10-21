from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=25)
	last_name = forms.CharField(max_length=25)
	email = forms.EmailField(max_length=150)

	# Clear the help text
	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)

		for field in ['username', 'password1', 'password2']:
			self.fields[field].help_text = None