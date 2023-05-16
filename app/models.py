from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=100)
    def __str__(self):
        return self.Topic_name