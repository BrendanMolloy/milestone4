from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from .forms import CommentForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from accounts.views import index

# Create your views here.

def all_products(request):
    """displays all products, applying pagination"""
    products_list = Product.objects.all().order_by('-price')
    paginator = Paginator(products_list, 9) # limits number of products to 9 per page
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {'products': products})

def all_accessory_products(request, category):
    """displays all products with the 'accessory' tag"""
    products_list = Product.objects.filter(tag=category)
    paginator = Paginator(products_list, 9) # limits number of products to 9 per page
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {'products': products})

def all_armor_products(request):
    """displays all products with the 'armor' tag"""
    products_list = Product.objects.filter(tag="armor")
    paginator = Paginator(products_list, 9) # limits number of products to 9 per page
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {'products': products})

def all_weapon_products(request):
    """displays all products with the 'weapon' tag"""
    products_list = Product.objects.filter(tag="weapon")
    paginator = Paginator(products_list, 9) # limits number of products to 9 per page
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {'products': products})

def product_detail(request, id):
    """
    Create a view that returns a single
    Product object based on the product ID and
    render it to the 'productdetail.html' template.
    Or return a 404 error if the product is
    not found
    """
    #requests the current product
    product = get_object_or_404(Product, pk=id)
    #requests all comments associated with current product
    comments = product.comments.filter(active=True)
    try:
        #requests current user's id
        user_id = request.user.pk 
        #requests current user
        current_user = User.objects.get(id=user_id)
    
        new_comment = None
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current product to the comment
                new_comment.product = product
                # Assign the current user to the comment
                new_comment.user = current_user
                # Save the comment to the database
                new_comment.save()
        else:
            comment_form = CommentForm()
        product.save()
        comment_form = CommentForm()
        return render(request, "productdetail.html", {'product': product, 
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form,})
    #renders the productdetail page without the comment form if user is not logged in
    except User.DoesNotExist:
        return render(request, "productdetail.html", {'product': product, 
                                                    'comments': comments})

@login_required(login_url=reverse_lazy("login"))
def edit_comment(request, id, pk):
    """
    This view allows users to edit their comment
    """
    product = get_object_or_404(Product, pk=id)
    #requests comment by pk
    comment = get_object_or_404(Comment, pk=pk)
    #assigns comment's pk to a variable
    comment_id = comment.pk
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            #redirects back to the associated product's page
            return redirect('../../')
        else:
            messages.error(request, "Please correct the highlighted errors:")
    else:
        # display the current comment details as they exist
        user_comment = Comment.objects.get(id=comment_id)
        comment_form = CommentForm(instance=user_comment)

    args = {"comment_form": comment_form}
    args.update(csrf(request))
    return render(request, "editcomment.html", args)

def delete_comment(request, id, pk):
    """
    This view renders the deletecomment page where the user must confirm that they wish to delete their comment
    """
    #requests comment by pk
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        comment.delete()
        #redirects back to the associated product's page
        return redirect('../../')
    context = {
        "object": comment
    }
    return render(request, "deletecomment.html", context)

