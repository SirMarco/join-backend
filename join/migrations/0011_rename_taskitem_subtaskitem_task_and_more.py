# Generated by Django 5.0.6 on 2024-08-02 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0010_remove_taskitem_subtasks_alter_subtaskitem_taskitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtaskitem',
            old_name='taskitem',
            new_name='task',
        ),
        migrations.RemoveField(
            model_name='taskitem',
            name='prio',
        ),
    ]
