from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ChangeForm(forms.ModelForm):
	class Meta:
		model = User 
		fields = ('username',)

		labels = {
			'username': ' Change your Username'
		}

class Register(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email',)
