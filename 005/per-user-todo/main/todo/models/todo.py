from django.contrib.auth.models import User as UserModel
from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=256)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
