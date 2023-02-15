from django.db import models

# Create your models here.

status_choices = [
    ('c', 'completed'),
    ('w', 'waiting'),
    ('p', 'on progress'),
]

priority_choices=[
    (1,'High'),
    (2,'Medium'),
    (3,'Low'),
]

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=priority_choices, default=1)
    status = models.CharField(choices=status_choices, default="w", max_length=1)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title