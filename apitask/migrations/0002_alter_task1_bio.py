# Generated by Django 4.1.2 on 2022-10-31 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task1',
            name='bio',
            field=models.CharField(max_length=300),
        ),
    ]
