from django import forms
from members.models import FeedBack

class CreateFeedBack(forms.ModelForm):
	class Meta:
		model = FeedBack
		fields = '__all__'

		widgets = {
			'user': forms.TextInput(attrs={'value': '', 'id': 'userid', 'type': 'hidden'}),
			'body': forms.Textarea(attrs={'class': 'form-control','rows':4, 'cols':20, 'placeholder': 'Enter Your FeedBack'})
		}

		labels = {
			'body': ''
		}