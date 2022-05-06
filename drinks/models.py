from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=350)

    # Change representation of object in the Model in Admin
    def __str__(self):
        return self.name
