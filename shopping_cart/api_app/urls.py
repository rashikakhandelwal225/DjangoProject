from django.urls import path
from .api_app_views import ShoppingCart, ShoppingCartUpdate, ShoppingCartDelete


urlpatterns = [
    path('cart_item/', ShoppingCart.as_view()),
    path('update-item/<int:item_id>', ShoppingCartUpdate.as_view()),
    path('delete/<int:item_id>', ShoppingCartDelete.as_view()),
]