from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import ChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import  login_required
from django.core.mail import send_mail

'''
class RegisterUser(CreateView):
	model = User
	form_class = UserCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
	'''

def Register(request):
	form = UserCreationForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect('login')
	return render(request, 'registration/register.html')

class ChangeUser(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = User
	# form_class = UserChangeForm
	form_class = ChangeForm
	template_name = 'registration/change.html'
	success_url = reverse_lazy('index')

	def get_context_data(self, *args, **kwargs):
		user = User.objects.all()
		context = super(ChangeUser, self).get_context_data(*args, **kwargs)
		page_user = get_object_or_404(User, id=self.kwargs['pk'])
		context['page_user'] = page_user
		return context

	success_message = 'Account was successfully Created! Please Login'

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
	model = User
	fields = '__all__'
	template_name = 'registration/change_password.html'
	success_url = reverse_lazy('index')

@login_required
def delete_user(request, pk):
	client = User.objects.get(id=pk)
	if request.user.id == client.id:
		client.delete()
		return redirect('logout')
	else:
		return redirect('index')
