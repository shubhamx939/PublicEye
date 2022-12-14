from django.db import models
from uuid import uuid4


# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(default=uuid4(), blank=False, null=False)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user_id)
    