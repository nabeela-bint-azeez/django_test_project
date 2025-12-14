from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_product,name='add'),
    path('list/',views.product_list,name='list'),
    path('update/<int:pk>/',views.update_product,name='update'),
    path('delete/<int:pk>/',views.delete_product,name='delete')
]
