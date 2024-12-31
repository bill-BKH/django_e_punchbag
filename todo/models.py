from django.db import models

# Create your models here.

class Todo(models.Model):
    Text = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    