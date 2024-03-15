from django.urls import path
from .views import home, todos, product, login, register, receptai_list, logout_view, create_recipe_view

urlpatterns = [
   path("", home, name="home"),
   path('todos/', todos, name='todos'),
   path('product/', product, name='product'),
   path('receptai/', receptai_list, name='receptai_list'),
   path('login/', login, name='login'),
   path('register/', register, name='register'),
   path('logout/', logout_view, name='logout'),
   path('create-recipe/', create_recipe_view, name='create_recipe'),
]
