# Generated by Django 5.0.6 on 2024-07-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('User', 'User'), ('Technical', 'Technical')], default='User', max_length=9, null=True),
        ),
    ]
