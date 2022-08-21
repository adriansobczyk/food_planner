from django.contrib import admin

from .models import Dish, DishCategory, DishIngredient, Ingredient, IngredientType

class DishIngredientsInline(admin.StackedInline):
    model = DishIngredient
    extra=0

class DishAdmin(admin.ModelAdmin):
    inlines = [
        DishIngredientsInline,
    ]
    readonly_fields = ('favourite', 'slug', 'date_creation')
admin.site.register(Dish, DishAdmin)

admin.site.register(DishCategory)
admin.site.register(Ingredient)
admin.site.register(IngredientType)