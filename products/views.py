from django.shortcuts import render, get_object_or_404
from .models import Product, Comment
from .forms import CommentForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def all_accessory_products(request):
    products = Product.objects.filter(tag="accessory")
    return render(request, "products.html", {"products": products})

def all_armor_products(request):
    products = Product.objects.filter(tag="armor")
    return render(request, "products.html", {"products": products})

def all_weapon_products(request):
    products = Product.objects.filter(tag="weapon")
    return render(request, "products.html", {"products": products})

def product_detail(request, pk):
    """
    Create a view that returns a single
    Product object based on the product ID (pk) and
    render it to the 'productdetail.html' template.
    Or return a 404 error if the product is
    not found
    """
    product = get_object_or_404(Product, pk=pk)
    # user = ForeignKey(User)
    user_id = request.user.pk 
    current_user = User.objects.get(id=user_id)
    # current_username = current_user.username
    
    comments = product.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            new_comment.user = current_user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    product.save()

    return render(request, "productdetail.html", {'product': product, 
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form,
                                            'user': current_user,})

@login_required(login_url=reverse_lazy("login"))
def edit_comment(request):
    """
    view to handle the form for users to edit their comment(s)
    """
    user_id = request.user.pk
      
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # save the new comment - but only if the user tried to change it!
            details = comment_form.save(commit=False)
            details.user = request.user
            details.save()
        else:
            messages.error(request, "Please correct the highlighted errors:")
    else:
        # display the user's current details, if they exist
        user_comment = Comment.objects.get(user=user_id)
        comment_form = CommentForm(instance=user_profile)

    args = {"comment_form": comment_form}
    args.update(csrf(request))
    return render(request, "editcomment.html", args)
