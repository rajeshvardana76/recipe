from django.urls import path
from . import views

urlpatterns = [

    path('menu/', views.menu, name='menu'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('<int:recipe_id>/detail/', views.detail, name='detail.html'),
    path('save_recipe/', views.save_recipe, name='save_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]
