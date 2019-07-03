from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import *

app_name = 'product'
urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product_add'),
    path('list/', my_product_list, name='products_list'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

]
