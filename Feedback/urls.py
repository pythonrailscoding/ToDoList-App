from django.urls import path
from . import views

urlpatterns = [
	path('list_feed/', views.Create, name='create-index'),
	path('edit_feed/<int:pk>/', views.edit, name='f_edit'),
	path('delete_feed/<int:pk>/', views.delete, name='delete-feed'),
]
