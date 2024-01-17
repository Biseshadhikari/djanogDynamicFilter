from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        return self.name
