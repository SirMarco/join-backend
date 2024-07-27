from django.contrib import admin
from .models import Category, Contact, SubTaskItem, TaskItem

# Register your models here.

admin.site.register(TaskItem)
admin.site.register(Category)
admin.site.register(SubTaskItem)
admin.site.register(Contact)