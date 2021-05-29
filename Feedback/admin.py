from django.contrib import admin
from members.models import FeedBack
from .models import FeedBackOnDelete

admin.site.register(FeedBack)
admin.site.register(FeedBackOnDelete)
