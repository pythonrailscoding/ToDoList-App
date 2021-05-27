from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

@login_required
def TaskList(request):
	object_list = TaskModel.objects.filter(user=request.user.id)
	form = TaskForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect('index')
	return render(request, 'task/index.html', {'object_list': object_list, 'form': form})

@login_required
def CrossItem(request, pk):
	item = TaskModel.objects.get(id=pk)
	if item.user.id == request.user.id:
		item.complete = True
		item.save()
	return redirect('index')

@login_required
def UncrossItem(request, pk):
	item = TaskModel.objects.get(id=pk)
	if item.user.id == request.user.id:
		item.complete = False
		item.save()
	return redirect('index')

@login_required
def deleteItem(request, pk):
	item = TaskModel.objects.get(id=pk)
	if item.user.id == request.user.id:
		item.delete()
	return redirect('index')

@login_required
def ClearList(request):
	item = TaskModel.objects.filter(user=request.user.id)
	for item in item:
		item.delete()
	return redirect('index')

@login_required
def delete_all_crossed_items(request):
	item = TaskModel.objects.filter(user=request.user.id)
	for item in item:
		if item.user.id == request.user.id and item.complete == True:
			item.delete()
	return redirect('index')

@login_required
def generate_text_file(request):
	response = HttpResponse(content_type="text/plain")
	response["Content-Disposition"] = "attachment; filename=generated_task_list.txt"

	lines = []
	item_list = TaskModel.objects.filter(user=request.user.id)

	for item in item_list:
		if item.complete == True:
			lines.append(f"Task Name: {item.title}\nStatus: Completed!\n\n\n")
		else:
			lines.append(f"Task Name: {item.title}\nStatus: Not Completed!\n\n\n")
	response.writelines(lines)

	return response


'''
def TaskCreate(request):
	form = TaskForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('index')
	return render(request, 'task/create.html', {'form': form})
'''
