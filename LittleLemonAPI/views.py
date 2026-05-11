from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User, Group

from .models import MenuItem, Category, Cart
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer


# 🍽 CATEGORY
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 🍔 MENU ITEMS
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [OrderingFilter]
    ordering_fields = ['price']


# 🛒 CART - MENU ITEMS (customer cart)
class CartMenuItemsView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        menuitem = serializer.validated_data['menuitem']
        quantity = serializer.validated_data['quantity']

        serializer.save(
            user=self.request.user,
            unit_price=menuitem.price,
            price=menuitem.price * quantity
        )


# 📦 CART - ORDERS (placeholder for now)
class CartOrdersView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # adjust later depending on your Order model
        return []

    def post(self, request, *args, **kwargs):
        return Response({"message": "Order endpoint works"})
        

# 👨‍🍳 MANAGER USERS
class ManagerUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        group = Group.objects.get(name="Manager")
        users = group.user_set.all()
        return Response([user.username for user in users])

    def post(self, request):
        username = request.data.get("username")

        user = User.objects.get(username=username)
        group = Group.objects.get(name="Manager")
        group.user_set.add(user)

        return Response({"message": f"{username} added to Manager group"})
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class OrdersView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return []

    def get(self, request, *args, **kwargs):
        return Response({"message": "Orders endpoint works"})


class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return Response({"message": f"Single order {pk} works"})

    def patch(self, request, pk):
        return Response({"message": f"Order {pk} updated"})