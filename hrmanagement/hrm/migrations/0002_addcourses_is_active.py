# Generated by Django 3.2.4 on 2022-11-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcourses',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
