# Generated by Django 5.0.6 on 2024-07-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('User', 'User'), ('Technical', 'Technical')], default='User', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
