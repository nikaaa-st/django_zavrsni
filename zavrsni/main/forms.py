from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_time', 'category', 'ingredients_text', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'ingredients_text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter ingredients'}),
        }