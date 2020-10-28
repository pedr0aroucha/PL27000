from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# Usar o ck editor para o app artigos


class Task(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    lastday = models.DateField(default=None)
    taskok = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
