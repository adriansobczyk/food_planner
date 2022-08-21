from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from taggit_autosuggest.managers import TaggableManager
from django.utils.translation import gettext as _

class IngredientType(models.Model):
    title = models.CharField(max_length=254)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)


class Ingredient(models.Model):
    title = models.CharField(max_length=254)
    date_creation = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(IngredientType, on_delete=models.CASCADE)  
    
    def __str__(self):
        return str(self.title)


class DishCategory(models.Model):
    title = models.CharField(max_length=254)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'dish category'
        verbose_name_plural = 'dish categories'
    

class Dish(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    # ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)
    slug = models.SlugField(unique=True, blank=True, max_length=254)
    favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='favourite_dish')
    
    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("dish_detail", kwargs={'slug': self.slug})


class DishIngredient(models.Model):
    UNIT_TYPE = (
        ('g', _('gram')),
        ('kg', _('kilogram')),
        ('ml', _('mililitr')),
        ('l', _('litr')),
        ('łyżeczka', _('łyżeczka')),
        ('łyżka', _('łyżka')),
        ('szklanka', _('szklanka')),
        ('sztuka', _('sztuka')),
    )
    quantity = models.IntegerField(verbose_name='ilość', default=1, blank=True)
    weight = models.IntegerField(verbose_name='waga', default=1, blank=True)
    unit_type = models.CharField(verbose_name='typ jednostki', choices=UNIT_TYPE, max_length=75, default=0, blank=True)
    related_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    related_dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.related_ingredient)