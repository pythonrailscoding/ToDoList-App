from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
	id = models.BigAutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.title + ' | ' + str(self.user) + ' | ' + str(self.complete)

