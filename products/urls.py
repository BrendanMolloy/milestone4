from django.conf.urls import url, include
from .views import all_products, product_detail, homepage

urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^all_products/', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail')
]