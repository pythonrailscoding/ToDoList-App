from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import ChangeForm, Register
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import  login_required
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth import login
from django.template.loader import render_to_string

'''
class RegisterUser(CreateView):
	model = User
	form_class = UserCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
	'''

class Register(FormView):
	template_name = 'registration/register.html'
	form_class = Register
	redirect_authenticated_user = True
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		template = render_to_string("registration/email.html", {"user": user.username})
		subject = 'You have signed up successfully! Congrats!'
		message = template
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [user.email, ]
		send_mail( subject, message, email_from, recipient_list )
		
		return super(Register, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('index')
		return super(Register, self).get(*args, **kwargs)


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
		template = render_to_string("registration/cancel_email.html", {"user": request.user.username})
		subject = 'Your account has been successfully deleted!'
		message = template
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [request.user.email, ]
		send_mail( subject, message, email_from, recipient_list )
		client.delete()
		return redirect('logout')
	else:
		return redirect('index')

def confirm_delete(request):
	return render(request, "registration/confirm_delete.html", {})
