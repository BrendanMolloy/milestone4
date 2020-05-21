from django.conf.urls import url, include
from .views import all_products, product_detail, all_accessory_products, all_armor_products, all_weapon_products, edit_comment, delete_comment

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^accessories/$', all_accessory_products, name='all_accessory_products'),
    url(r'^armor/$', all_armor_products, name='all_armor_products'),
    url(r'^weapons/$', all_weapon_products, name='all_weapon_products'),
    url(r'^(?P<id>\d+)/$', product_detail, name='product_detail'),
    url(r'^(?P<id>\d+)/edit_comment/(?P<pk>\d+)/$', edit_comment, name='edit_comment'),
    url(r'^(?P<id>\d+)/delete_comment/(?P<pk>\d+)/$'', delete_comment, name='delete_comment'),
]