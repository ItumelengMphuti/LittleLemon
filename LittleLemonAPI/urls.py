from django.urls import path
from .views import (
    MenuItemsView,
    SingleMenuItemView,
    CategoryView,
    CartMenuItemsView,
    CartOrdersView,
    ManagerUsersView,
    OrdersView,
    SingleOrderView
)

urlpatterns = [

    # MENU ITEMS
    path('menu-items', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),

    # CATEGORIES
    path('categories', CategoryView.as_view()),

    # CART
    path('cart/menu-items', CartMenuItemsView.as_view()),
    path('cart/orders', CartOrdersView.as_view()),

    # ORDERS
    path('orders', OrdersView.as_view()),
    path('orders/<int:pk>', SingleOrderView.as_view()),

    # MANAGERS
    path('groups/manager/users', ManagerUsersView.as_view()),
]