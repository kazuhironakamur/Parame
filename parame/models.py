from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class Sheet(models.Model):
    project = models.ForeignKey(
        'parame.Project',
        on_delete=models.CASCADE,
        related_name='sheets',
        default=1
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name