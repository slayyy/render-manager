from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    pass
    # add additional fields in here
    is_student = models.BooleanField(null=True)
    is_teacher = models.BooleanField(null=True)

    def __str__(self):
        return self.email

class Render(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    note = models.IntegerField()
    comment = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title


class GroupRender(models.Model):
    student = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    body = models.TextField()
    note = models.IntegerField()
    comment = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title
