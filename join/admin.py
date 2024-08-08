from django.contrib import admin
from .models import Contact, TaskItem

# Register your models here.

admin.site.register(TaskItem)
admin.site.register(Contact)