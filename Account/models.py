from django.db import models



# Create your models here.
class User(models.Model):
    from uuid import uuid4
    user_id = models.UUIDField(default=uuid4(), blank=False, null=False)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user_id)


class ToDo(models.Model):
    from uuid import uuid4
    to_id = models.UUIDField(default=uuid4(), blank=False, null=False)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    datetime = models.CharField(max_length=100, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.to_id)