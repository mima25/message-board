# posts/models.py
from django.db import models


class Post(models.Model):  # new
    text = models.TextField()

    def __str__(
        self,
    ):  # best practice to add str() methods to all of your models to improve their readability.
        return self.text[:50]
