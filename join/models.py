from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  class Category_Choices(models.TextChoices):
    USER = 'User', ('User')
    TECHNICAL = 'Technical', ('Technical')
  name = models.CharField(
  max_length=9,
  choices=Category_Choices.choices,
  default=Category_Choices.USER,
  ) 
  color =models.CharField(max_length=9)

  def __str__(self):
      return self.name

class TaskItem(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  due_date = models.DateField()
  class Priority(models.TextChoices):
    LOW = 'Low', ('Low')
    MEDIUM = 'Medium', ('Medium')
    Urgent = 'Urgent', ('Urgent')
  priority = models.CharField(
    max_length=9,
    choices=Priority.choices,
    default=Priority.LOW,
  )
  category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
  assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 
  users = models.ManyToManyField(User, related_name='TaskItem')

  def __str__(self):
      return self.title

class SubTaskItem(models.Model):
  title = models.CharField(max_length=100)
  taskitem = models.ForeignKey(TaskItem, related_name='subtask', on_delete=models.CASCADE)

  def __str__(self):
      return self.title

class Contact(models.Model):
  user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)

  def __str__(self):
    return self.first_name

