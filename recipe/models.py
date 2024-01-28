import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractModel(models.Model):
    id = models.UUIDField(_('ID'), primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        abstract = True


class Recipe(AbstractModel):
    name = models.CharField(_('Recipe Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)
    count = models.IntegerField(_('Times used'), default=0)

    class Meta:
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipes')

    def __str__(self):
        return self.name


class Product(AbstractModel):
    name = models.CharField(_('Product Name'), max_length=255)
    description = models.TextField(_('Description'), blank=True, null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Ingredient(AbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField(_('Weight'), blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
        unique_together = ('product', 'recipe')

    def __str__(self):
        return self.product.name
