from django.conf.urls import url, include
from .views import all_products, product_detail, homepage

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail')
]