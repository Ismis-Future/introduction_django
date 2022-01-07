from typing import ContextManager
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    Content = models.TextField()