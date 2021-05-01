from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    process = models.TextField()
    images = models.ImageField(upload_to="media/", default=timezone.now())

    def __str__(self):
        return self.recipe_name