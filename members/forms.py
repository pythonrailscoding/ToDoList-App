from django import forms
from django.contrib.auth.models import User

class ChangeForm(forms.ModelForm):
	class Meta:
		model = User 
		fields = ('username',)

		labels = {
			'username': ' Change your Username'
		}
