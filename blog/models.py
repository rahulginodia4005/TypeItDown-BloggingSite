from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    author_name = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
