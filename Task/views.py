from django.shortcuts import render, redirect
from rest_framework import serializers
from .models import TaskModel
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, FileResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskModelSerializers
from django.contrib.auth.models import User
import csv
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
import io

@login_required
def TaskList(request):
	object_list = TaskModel.objects.filter(user=request.user.id).order_by('id')
	form = TaskForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			search = request.POST["searched"]
			object_list = TaskModel.objects.filter(user=request.user.id).filter(title__contains=search).order_by('id')
		
			
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
			lines.append(f"Task Name: {item.title}\n Status: Completed!\n\n\n")
		else:
			lines.append(f" Task Name: {item.title}\n Status: Not Completed!\n\n\n")
	response.writelines(lines)

	return response

@login_required
@api_view(["GET"])
def api_list(request):
	user_task_list = TaskModel.objects.filter(user=request.user.id)
	serializer = TaskModelSerializers(user_task_list, many=True)
	return Response(serializer.data)

@login_required
@api_view(["GET"])
def individual_api_list(request, pk):
	item = TaskModel.objects.get(id=pk)
	if item.user.id == request.user.id:
		serializer = TaskModelSerializers(item, many=False)
		return Response(serializer.data)
	else:
		return redirect("index") 

'''
def TaskCreate(request):
	form = TaskForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('index')
	return render(request, 'task/create.html', {'form': form})
'''

@login_required
@api_view(["POST"])
def api_create(request):
	serializer = TaskModelSerializers(data=request.data)
	user_current = User.objects.get(id=request.user.id)
	if serializer.is_valid():
		serializer.save(user=user_current)
		return Response("Success! Item was submitted Successfully!")
	else:
		return Response("Item not Submitted Successfully! Maybe, User ID is incorrect or not available. Check for Syntax errors!")

@login_required
def api_views_list(request):
	return render(request, "task/api_file.html", {})

@login_required
def generate_csv_file(request):
	response = HttpResponse(content_type="text/csv")
	response["Content-Disposition"] = "attachment; filename=generated_task_list.csv"
	# Create a csv writer
	writer = csv.writer(response)
	
	item_list = TaskModel.objects.filter(user=request.user.id)

	writer.writerow(["Task Name", "Status"])

	for item in item_list:
		if item.complete == True:
			writer.writerow([item.title, "Completed!"])
		else:
			writer.writerow([item.title, "Not Completed!"])

	return response

"""@login_required
@api_view(["POST"])
def api_update(request, pk):
	item = TaskModel.objects.get(id=pk)
	if item:
		if item.user.id == request.user.id:
			serializer = TaskModelSerializers(instance=item, data=request.data)
			user_current = User.objects.get(id=request.user.id)
			if serializer.is_valid():
				serializer.save(user=user_current)
				return Response("Success! Item was submitted Successfully!")
			else:
				return Response("Item not Submitted! Maybe, User ID is incorrect or not avauilable. Check for Syntax errors!")
		else:
			return redirect("index")
	else:
		return redirect("index")"""

@login_required
def generate_pdf_file(request):
	buf = io.BytesIO()
	c = Canvas(buf, pagesize=letter, bottomup=0)
	# Create a Text Object
	textobj = c.beginText()
	textobj.setTextOrigin(inch, inch)

	textobj.setFont("Helvetica", 14)

	lines = []
	item_list = TaskModel.objects.filter(user=request.user.id)

	for item in item_list:
		if item.complete == True:
			lines.append(f"Task Name: {item.title}")
			lines.append("Status: Completed!")
			lines.append(" ")
		else:
			lines.append(f"Task Name: {item.title}")
			lines.append("Status: Not Completed!")
			lines.append(" ")
		
	for line in lines:
		textobj.textLine(line)

	c.drawText(textobj)
	c.showPage()
	c.save()
	buf.seek(0)

	return FileResponse(buf, as_attachment=True, filename="generated_task_list.pdf")
