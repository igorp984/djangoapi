from django.urls import path
from . import views

urlpatterns = [
    path('api/item/', views.ItemListCreate.as_view() ),
    path('api/pedido/', views.PedidoListCreate.as_view()),
]
