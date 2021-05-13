from django.db import models

class Reporting(models.Model):
    Student_Name = models.CharField(max_length=64)
    Behavior_Desc = models.CharField(max_length=256)
    Comments = models.TextField()