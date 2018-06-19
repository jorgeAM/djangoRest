from django.urls import path
from compras import views

urlpatterns = [
    path('clients/', views.client_list),
]
