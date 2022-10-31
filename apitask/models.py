from django.db import models

# Create your models here.
class Task1(models.Model):
    slackUsername=models.CharField(max_length=25)
    backend=models.BooleanField(default=True)
    age=models.IntegerField(default=0)
    bio=models.CharField(max_length=25)

    def __str__(self):
        return self.slackUsername

from django.contrib import admin
admin.site.register(Task1)