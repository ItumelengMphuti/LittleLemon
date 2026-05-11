from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter
from .models import MenuItem, Category, Cart
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [OrderingFilter]
    ordering_fields = ['price']
    
class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        menuitem = serializer.validated_data['menuitem']
        quantity = serializer.validated_data['quantity']

        unit_price = menuitem.price
        price = unit_price * quantity

        serializer.save(
            user=self.request.user,
            unit_price=unit_price,
            price=price
        )