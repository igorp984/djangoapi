from django.urls import path
from . import views

urlpatterns = [
    path('api/produto/', views.ProdutoListCreate.as_view() ),
]
