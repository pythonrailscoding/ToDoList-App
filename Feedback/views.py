from django.shortcuts import render, redirect
from members.models import FeedBack
from .forms import CreateFeedBack
from django.contrib.auth.decorators import login_required

def Create(request):
	list_feed = FeedBack.objects.all().order_by('-id')
	form = CreateFeedBack(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
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



