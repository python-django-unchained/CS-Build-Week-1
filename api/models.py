from django.db import models
from django import forms
from uuid import uuid4

# Create your models here.
class Cowboy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def initialize(self):
        self.save()

    # def register(self):
    #     pass

    # def login(self):
    #     pass

    # def logout(self):
    #     pass