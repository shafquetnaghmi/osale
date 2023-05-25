from django.shortcuts import render
from .models import FeaturedProduct,Product


def shop(request):
    featured_product=Product.objects.all()
    context={'featured_product':featured_product}
    return render(request,'shop/shop.html',context)


