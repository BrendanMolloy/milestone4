from django.conf.urls import url, include
from .views import all_products, product_detail, products_weapon, products_armor, products_accessory

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^weapons/$', products_weapon, name='all_weapons'),
    url(r'^armor/$', products_armor, name='all_armor'),
    url(r'^accessories/$', products_accessory, name='all_accessories'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail')
]