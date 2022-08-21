from urllib import request
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import List


class ShoppingListView(LoginRequiredMixin, ListView):
    model = List
    template_name = 'shopping_list/ShoppingListView.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the lists
        context['lists'] = List.objects.filter(user_id=self.request.user)
        return context


class ShoppingDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = 'shopping_list/ShoppingDetailView.html'
    context_object_name = 'list'