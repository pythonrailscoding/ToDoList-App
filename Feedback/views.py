from django import template
from django.shortcuts import render, redirect
from members.models import FeedBack
from .forms import CreateFeedBack
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import FeedBackOnDelete

def Create(request):
	list_feed = FeedBack.objects.all().order_by('-id')
	form = CreateFeedBack(request.POST or None)
	template = render_to_string("email.html", {"user": request.user.username})
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			email = EmailMessage(
				"Thanks for your feedback!",
				template,
				settings.EMAIL_HOST_USER,
				[request.user.email,],
			)
			email.fail_silently = False
			email.send()
		return redirect('create-index')
	# ordering = ['-id']
	return render(request, 'list.html', {'list_feed': list_feed, 'form': form})

@login_required
def edit(request, pk):
	item = FeedBack.objects.get(id=pk)
	if item.user.id == request.user.id:
		form = CreateFeedBack(request.POST or None, instance=item)
		if request.method == 'POST':
			if form.is_valid():
				form.save()
			return redirect('create-index')
	else:
		return redirect('create-index')
	return render(request, 'edit.html', {'form': form})

@login_required
def delete(request, pk):
	item = FeedBack.objects.get(id=pk)
	if item.user.id == request.user.id:
		# form = CreateFeedBack(request.POST or None, instance=item)
		item.delete()
		return redirect('create-index')
	else:
		return redirect('create-index')

def feedback_on_delete(request):
	if request.method == 'POST':
		feed = request.POST["feed"]
		new = FeedBackOnDelete.objects.create(feed=feed,)
		new.save()
		return redirect("success")
	return render(request, "del.html", {})

def success_post(request):
	return render(request, "feedback_revert.html", {})



