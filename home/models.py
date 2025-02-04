from django.db import models


class users (models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


