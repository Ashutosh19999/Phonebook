from django.db import models

# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length=30)
    mobileno=models.BigIntegerField()
    def __str__(self):
        return self.name