from django.db import models


class TodoItems(models.Model):
    objects = None
    content = models.TextField()
