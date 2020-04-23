from django.shortcuts import render, get_object_or_404
from .models import Product, Comment
from .forms import CommentForm
from django.contrib.auth.models import User

# Create your views here.
def all_products(request):
    products = Product.objects.all()
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
    user_id = request.user.pk 
    current_user = User.objects.get(user=user_id)
    
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
            new_comment.user = user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    product.save()

    return render(request, "productdetail.html", {'product': product, 
                                            'user': current_user.username,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})