from django.contrib import admin
from .models import Product, Comment

# Register your models here.
admin.site.register(Product)
admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'product', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'body')
