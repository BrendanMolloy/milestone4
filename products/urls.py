from django.conf.urls import url, include
from .views import all_products, product_detail, all_weapon_products

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^weapons/$', all_weapon_products, name='all_weapon_products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail')
]