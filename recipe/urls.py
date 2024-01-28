from django.urls import path

from .views import *


urlpatterns = [
    path('show-recipes-without-product/<uuid:product_id>/', RecipesWithoutProductAPIView.as_view()),
    path('add-product-to-recipe/', AddProductAPIView.as_view()),
    path('cook-recipe/<uuid:recipe_id>', CookRecipeAPIView.as_view()),
    path('recipes/', RecipeListAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('ingredients/', IngredientListAPIView.as_view()),
]
