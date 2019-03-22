from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.ItemList.as_view(), name='items_index'),
    path('add/', views.ItemCreate.as_view(), name='item_create'),
    path('delete/<int:item_id>', views.item_delete, name='item_delete'),
]