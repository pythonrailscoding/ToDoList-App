from django.urls import path
from . import views

urlpatterns = [
	path('', views.TaskList, name='index'),
	# path('create', views.TaskCreate, name='create'),
	path('cross_item/<int:pk>', views.CrossItem, name='cross'),
	path('uncross_item/<int:pk>', views.UncrossItem, name='uncross'),
	path('delete_item/<int:pk>', views.deleteItem, name='delete'),
	path('delete_all_crossed_items/', views.delete_all_crossed_items, name='delete_all_crossed_items'),
	path('clear_list/', views.ClearList, name='ClearList'),
	path("generate_text_file/", views.generate_text_file, name="generate_text_file"),
]
