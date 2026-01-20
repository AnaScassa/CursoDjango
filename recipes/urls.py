from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/search/', lambda request: ..., name="search"),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
    path('category/<int:category_id>/', views.category, name='category'),

     #lambda = function test
]
