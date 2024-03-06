from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title