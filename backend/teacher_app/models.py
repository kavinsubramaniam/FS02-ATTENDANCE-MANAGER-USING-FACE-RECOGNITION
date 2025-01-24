from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
