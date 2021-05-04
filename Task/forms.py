from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
	class Meta:
		model = TaskModel
		fields = ('user', 'title',)

		widgets = {
			'user': forms.TextInput(attrs={'value': '', 'id': 'userid', 'type': 'hidden'}),
			'title': forms.TextInput(attrs={})
		}

		labels = {
			'title': ''
		}
