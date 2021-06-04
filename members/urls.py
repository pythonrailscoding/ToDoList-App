from django.urls import path
from .views import ChangeUser, ChangePassword, Register
from . import views
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView 

urlpatterns = [
	# path('register', RegisterUser.as_view(), name='register'),
	path('register', Register.as_view(), name='register'),
	path('change_user_credentials/<int:pk>/', ChangeUser.as_view(), name='change_user_credentials'),
	path('change_user_credentials/password/<int:pk>/', ChangePassword.as_view(), name='password'),
	path('delete_user/<int:pk>/', views.delete_user, name='del'),
	path("confirm_user_delete/", views.confirm_delete, name="con"),
	path('password_reset/',PasswordResetView.as_view(template_name="accounts/password_reset.html"),name='password_reset'),
	path('password_reset_done/', PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),name='password_reset_confirm'),
	path('reset/done/', PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),name='password_reset_complete'),
	
]
