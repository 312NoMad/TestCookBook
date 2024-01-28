# Generated by Django 5.0.1 on 2024-01-27 23:51

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Recipe Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('count', models.IntegerField(default=0, verbose_name='Times used')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Product Weight')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='recipe.recipe')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'unique_together': {('recipe', 'name')},
            },
        ),
    ]