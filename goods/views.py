from django.shortcuts import render

from goods.models import Product

# Create your views here.


def menu(request):
    goods = Product.objects.all()
    context = {
        "title": "Меню",
        "goods": goods,
    }
    return render(request, "goods/menu.html", context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)


    context = {
        "product": product,
    }
    return render(request, "goods/product.html", context=context)
