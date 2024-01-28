from django.contrib import admin

from .models import Recipe, Product, Ingredient


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


class IngredientInline(admin.TabularInline):
    model = Ingredient
    can_delete = True
    verbose_name_plural = 'ingredients'
    fk_name = 'recipe'


@admin.register(Recipe)
class RecordAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
