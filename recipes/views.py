from django.shortcuts import render
from .models import Recipes
from django.http import HttpResponseRedirect, HttpResponse

def menu(request):
    recipes = Recipes.objects.all()
    return render(request, "recipes/menu.html", {'recipes': recipes})


def create_recipe(request):
    return render(request, "recipes/create.html")

def save_recipe(request):
    Recipes.objects.create(recipe_name=request.POST['name'],
                           ingredients=request.POST['ingredients'],
                           process=request.POST['process'])
    return HttpResponseRedirect("/recipes/menu")

def detail(request, recipe_id):
    recipe_detail = Recipes.objects.get(id=recipe_id)
    return render(request, "recipes/detail.html", {'recipes': recipe_detail})

def delete_recipe(request, recipe_id):
    Recipes.objects.get(id=recipe_id).delete()
    return HttpResponseRedirect("/recipes/menu")