from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    """
    The Product model stores the information associated with each product
    The attributes include:
        name: product's name
        description: a description of the product
        tag: the associated tag of the product,
        allows products to be iltered by "accessory", "armor", or "weapon"
        price: the cost of the product
        image: the image of the product
    """
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    tag = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    The Comment model stores the nformation associated with each comment
    The attributes include:
        product: the product that the comment is associated with
        user: the user that created the comment
        body: the text of the comment
        created_on: the time the comment was created, used to sort comments
        active: a boolean field that is set to true by default,
        can be set to false by admin to hide comment
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
