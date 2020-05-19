from django.conf.urls import url, include
from .views import all_products, product_detail, all_accessory_products, all_armor_products, all_weapon_products, edit_comment

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^accessories/$', all_accessory_products, name='all_accessory_products'),
    url(r'^armor/$', all_armor_products, name='all_armor_products'),
    url(r'^weapons/$', all_weapon_products, name='all_weapon_products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^(?P<pk>\d+)edit_comment/$', edit_comment, name='edit_comment'),
]