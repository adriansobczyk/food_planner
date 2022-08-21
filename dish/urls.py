from django.urls import path

from . import views


urlpatterns = [
    path('przepisy/', views.DishListView.as_view(), name='dish_list'),
    path('przepis/<slug:slug>/', views.DishDetailView.as_view(), name='dish_detail'),
    path('przepis-dodaj/', views.DishCreateView.as_view(), name='dish_create'),
    path('przepis/<slug:slug>/edytuj', views.DishUpdateView.as_view(), name='dish_update'),
    path('przepis/<slug:slug>/usun', views.DishDeleteView.as_view(), name='dish_delete'),
    path('search/', views.search, name="search_results"),

]