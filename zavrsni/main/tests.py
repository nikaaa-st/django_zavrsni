from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12345')
        self.category = Category.objects.create(name='Deserti')
        self.recipe = Recipe.objects.create(
            title='Kolač',
            description='Opis',
            preparation_time=30,
            category=self.category,
            author=self.user
        )

    def test_recipe_str(self):
        self.assertEqual(str(self.recipe), 'Kolač')
