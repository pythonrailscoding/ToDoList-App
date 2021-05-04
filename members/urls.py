from django.urls import path
from .views import ChangeUser, ChangePassword
from . import views

urlpatterns = [
	# path('register', RegisterUser.as_view(), name='register'),
	path('register', views.Register, name='register'),
	path('change_user_credentials/<int:pk>/', ChangeUser.as_view(), name='change_user_credentials'),
	path('change_user_credentials/password/<int:pk>/', ChangePassword.as_view(), name='password'),
	path('delete_user/<int:pk>/', views.delete_user, name='del'),
]
