from django.db.models import Q
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from .models import Product, Recipe, Ingredient
from .serializers import RecipeSerializer, ProductSerializer, IngredientSerializer


__all__ = [
    'AddProductAPIView',
    'RecipeListAPIView',
    'ProductListAPIView',
    'IngredientListAPIView',
    'CookRecipeAPIView',
    'RecipesWithoutProductAPIView'
]


class AddProductAPIView(GenericAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get(self, request, *args, **kwargs):
        recipe_id = request.data.get('recipe_id')
        product_id = request.data.get('product_id')
        weight = request.data.get('weight')

        ingredient = Ingredient.objects.filter(
            recipe=recipe_id,
            product=product_id
        ).first()
        if ingredient:
            ingredient.weight = weight
            ingredient.save()
            recipe = Recipe.objects.filter(id=recipe_id).first()
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data)
        ingredient = Ingredient.objects.create(
            recipe=Recipe.objects.get(id=recipe_id),
            product=Product.objects.get(id=product_id),
            weight=weight
        )
        serializer = IngredientSerializer(ingredient)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        new_recipe = Recipe.objects.filter(id=recipe_id).first()
        serializer = RecipeSerializer(new_recipe)
        return Response(serializer.data)


class CookRecipeAPIView(GenericAPIView):
    serializer_class = RecipeSerializer

    def get(self, request, recipe_id, *args, **kwargs):
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.count += 1
        recipe.save()
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)


class RecipesWithoutProductAPIView(APIView):

    def get(self, request, product_id, *args, **kwargs):
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response(status=400, data={'message': 'Product does not exist'})
        recipes = Recipe.objects.filter(
            Q(ingredients__product=product) & Q(ingredients__weight__lt=10)
        )
        other_recipes = Recipe.objects.exclude(ingredients__product=product)
        recipes = recipes.union(other_recipes)
        return render(request, 'recipe/recipes.html', {'recipes': recipes, 'product': product})


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class IngredientListAPIView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
