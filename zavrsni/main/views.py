from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe, Category, Ingredient
from .forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class RecipeListView(ListView):
    model = Recipe
    template_name = "main/recipe_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "main/recipe_detail.html"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "main/recipe_form.html"
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "main/recipe_form.html"
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "main/recipe_confirm_delete.html"
    success_url = reverse_lazy('recipe-list')

class RecipeSearchView(ListView):
    model = Recipe
    template_name = "main/partials/recipe_results.html"

    def get_queryset(self):
        q = self.request.GET.get("q")
        return Recipe.objects.filter(title__icontains=q)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

class CategoryListView(ListView):
    model = Category
    template_name = "main/category_list.html"

class RecipesByCategoryView(ListView):
    model = Recipe
    template_name = "main/recipes_by_category.html"

    def get_queryset(self):
        self.category = Category.objects.get(pk=self.kwargs["pk"])
        return Recipe.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


class IngredientListView(ListView):
    model = Ingredient
    template_name = "main/ingredient_list.html"
