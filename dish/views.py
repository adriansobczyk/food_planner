from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404 , render
from .models import Dish
from .forms import DishForm
from django.urls import reverse_lazy
from django.db.models import Q

class DishListView(ListView):
    template_name = 'dish/DishListView.html'
    model = Dish
    
    def get_context_data(self, **kwargs):
            context = super(DishListView, self).get_context_data(**kwargs)
            dish_list = Dish.objects.all()
            context['dish_list'] = dish_list
            return context

class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish/DishDetailView.html'

class DishCreateView(CreateView):
    form_class = DishForm
    queryset = Dish.objects.all()
    template_name = 'dish/DishCreateView.html'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class DishUpdateView(UpdateView):
    form_class = DishForm
    queryset = Dish.objects.all()
    template_name = 'dish/DishUpdateView.html'
    
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Dish, slug=slug)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'dish/DishDeleteView.html'
    success_url = reverse_lazy('dish_list')

# class SearchView(ListView):
#     model = Dish
#     template_name = "search/SearchView.html"
#     context_object_name = 'searched_dishes'

#     def get_queryset(self): 
#         query = self.request.GET.get("query")
#         object_list = Dish.objects.filter(
#             Q(title__icontains=query) | Q(description__icontains=query)
#         )
#         return object_list

def search(request):

    results = []

    if request.method == "GET":
        query = request.GET.get('query')
        if query == '':
            query = 'None'
        results = Dish.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'search/SearchView.html', {'query': query, 'search_results': results})