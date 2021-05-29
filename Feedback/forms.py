from django import forms
from members.models import FeedBack
from .models import FeedBackOnDelete

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

class FeedBackModelForm(forms.ModelForm):
	class Meta:
		model = FeedBackOnDelete
		fields = '__all__'

		widgets = {
			'feed': forms.Textarea(attrs={"class": "form-control", "rows": 4, "cols":20, "placeholder": "Enter Feedback"}),
		}

		labels = {
			"feed": "",
		}


