from django.shortcuts import render

from django.http.response import  JsonResponse

from . import models


products = models.Product.objects.all()
categories = models.Category.objects.all()


def product_list(request):
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = models.Product.objects.get(id=product_id)
    except models.Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(product.to_json())


def category_list(request):
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = models.Category.objects.get(id=category_id)
    except models.Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(category.to_json())
# Create your views here.
