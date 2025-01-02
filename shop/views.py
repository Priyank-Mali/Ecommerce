from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from django.contrib import messages

def home(request):
    productQueryset = Product.objects.all()
    grouped_product = {}
    for product in productQueryset:
        if product.category not in grouped_product:
            grouped_product[product.category] = []
        grouped_product[product.category].append(product)

    context = {
        "products" : grouped_product
    }
    return render(request,"shop/index.html",context)


def product_detail_page(request,id):
    myproduct = Product.objects.get(product_id = id)
    context = {
        "product" : myproduct
    }
    return render(request,"shop/productDetail.html",context)

def contact_me_page(request):
    if request.method == "POST":
        name_ = request.POST.get("name")
        email_ = request.POST.get("email")
        mobile_ = request.POST.get("mobile")
        text_ = request.POST.get("text")

        Contact.objects.create(
            name = name_,
            email = email_,
            mobile = mobile_,
            question = text_
        )
        messages.success(request,"Thank you For Contact US!")

    return render(request,"shop/contactPage.html")


def checkOut_page(request):
    return render(request,'shop/checkout.html')