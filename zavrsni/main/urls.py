from django.urls import path
from .views import CategoryListView, IngredientListView, RecipeListView, RecipeDetailView, RecipeCreateView, RecipeSearchView, RecipeUpdateView, RecipeDeleteView, RecipesByCategoryView, register

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('register/', register, name='register'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('ingredients/', IngredientListView.as_view(), name='ingredient-list'),
    path('search/', RecipeSearchView.as_view(), name='recipe-search'),
    path("categories/<int:pk>/recipes/", RecipesByCategoryView.as_view(), name="recipes-by-category"),

]
