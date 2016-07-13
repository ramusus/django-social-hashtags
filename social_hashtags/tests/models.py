"""
Model for testing purposes
"""
from django.db import models


class Post(models.Model):
    message = models.TextField()
