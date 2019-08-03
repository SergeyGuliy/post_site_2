from django.urls import path, include
from django.views.generic import TemplateView
from store.views import (
    category_view,
    product_view,
    parent_category_view,
    cart_view,
    add_to_cart_view,
    remove_from_cart_view,
    change_item_quantity,
    checkout_view,
    make_order_view,
    account_view,
    logout_view)

urlpatterns = [
    path('category/<category_slug>/', category_view, name='category_detail'),
    path('product/<product_slug>/', product_view, name='product_detail'),
    path('<parent_category_slug>', parent_category_view, name='parent_category_detail'),
    path('add_to_cart/', add_to_cart_view, name='add_to_cart'),
    path('remove_from_cart/', remove_from_cart_view, name='remove_from_cart'),
    path('change_item_quantity/', change_item_quantity, name='change_item_quantity'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('make_order/', make_order_view, name='make_order'),
    path('thank_you/', TemplateView.as_view(template_name='thank_you.html'), name='thank_you'),
    path('account/', account_view, name='account'),
    path('logout/', logout_view, name='logout')
]