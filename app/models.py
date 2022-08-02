# Create your models here.
from operator import mod
from statistics import mode

from django.contrib.auth.models import User
from django.db import models


class TODO(models.Model):
    status_choice = [
    ('c', 'complete'),
    ('p', 'pending'),
    ]

    priority_choice = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ]

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choice)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_choice)
