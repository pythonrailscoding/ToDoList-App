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
	path("api-list/", views.api_list, name='api-list'),
	path("individual_api_list/<int:pk>/", views.individual_api_list, name="api-ind"),
	path("create-api/", views.api_create, name="create-api"),
	path("api_views_list/", views.api_views_list, name="api"),
	#path('api_update_view/<int:pk>/', views.api_update, name="api_update"),
	path("generate_csv_file/", views.generate_csv_file, name="generate_csv_file"),
	path("generate_pdf_file/", views.generate_pdf_file, name="generate_pdf_file"),
]
