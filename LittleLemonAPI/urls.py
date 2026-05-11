from django.urls import path
from .views import MenuItemsView, CategoryView, CartView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('menu-items/', MenuItemsView.as_view()),
    path('cart/', CartView.as_view()),
]