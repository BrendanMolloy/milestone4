from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    products_list = Product.objects.filter(name__icontains=request.GET['q'])
    paginator = Paginator(products_list, 9) # limits number of products to 9 per page
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})