from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    USER = 'User'
    TECHNICAL = 'Technical'
    CHOICES = (
        (USER, "User"),
        (TECHNICAL, "Technical"),
    )
    name = models.CharField(
        max_length=9,
        null=True,
        choices=CHOICES,
        default="User",
    )
    color = models.CharField(max_length=9)

    def __str__(self):
        return self.name

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class TaskItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    due_date = models.DateField()
    
    class Priority(models.TextChoices):
        LOW = 'Low', ('Low')
        MEDIUM = 'Medium', ('Medium')
        URGENT = 'Urgent', ('Urgent')
    priority = models.CharField(
        max_length=9,
        choices=Priority.choices,
        default=Priority.LOW,
    )
    
    class Progress(models.TextChoices):
        TODO = 'Todo', ('ToDo')
        INPROGRESS = 'inProgress', ('In Progress')
        AWAITFEEDBACK = 'Await_Feedback', ('Await Feedback')
        DONE = 'Done', ('Done')
    progress = models.CharField(
        max_length=14,
        choices=Progress.choices,
        default=Progress.TODO,
    )
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(Contact, related_name='assigned_tasks')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class SubTaskItem(models.Model):
    parent_task = models.ForeignKey(TaskItem, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
