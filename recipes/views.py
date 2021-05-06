from django.shortcuts import render
from .models import Recipes
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    return render(request, "recipes/login.html")


def register_page(request):
    return render(request, "recipes/register.html")


def save_data(request):
    User.objects.create_user(username=request.POST['username'],
                             password=request.POST['password'],
                             email=request.POST['email'])
    return HttpResponseRedirect("/recipes/")


def login_status(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/recipes/menu/")
    else:
        return HttpResponse("<h3>your username and password did not match</h3>")

def menu(request):
    recipes = Recipes.objects.all()
    return render(request, "recipes/menu.html", {'recipes': recipes})


def create_recipe(request):
    return render(request, "recipes/create.html")

def save_recipe(request):
    Recipes.objects.create(recipe_name=request.POST['name'],
                           ingredients=request.POST['ingredients'],
                           process=request.POST['process'],
                           images=request.FILES['image'])

    return HttpResponseRedirect("/recipes/menu")

def detail(request, recipe_id):
    recipe_detail = Recipes.objects.get(id=recipe_id)
    return render(request, "recipes/detail.html", {'recipes': recipe_detail})

def delete_recipe(request, recipe_id):
    Recipes.objects.get(id=recipe_id).delete()
    return HttpResponseRedirect("/recipes/menu")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/recipes/")