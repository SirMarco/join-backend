# Generated by Django 5.0.6 on 2024-08-02 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0009_remove_taskitem_subtasks_taskitem_subtasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskitem',
            name='subtasks',
        ),
        migrations.AlterField(
            model_name='subtaskitem',
            name='taskitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='join.taskitem'),
        ),
    ]
