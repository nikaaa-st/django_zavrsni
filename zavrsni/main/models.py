from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Description of the recipe")
    preparation_time = models.PositiveIntegerField(help_text="Time in minutes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ingredients_text = models.TextField(blank=True, help_text="Enter ingredients")
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        related_name="ingredients",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
