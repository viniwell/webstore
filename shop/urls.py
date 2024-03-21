from django.urls import path

from . import views as v

app_name='shop'

urlpatterns = [
    path('', v.product_list, name='product_list'),
    path('<slug:category_slug>/', v.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', v.product_detail, name='product_detail')
]
