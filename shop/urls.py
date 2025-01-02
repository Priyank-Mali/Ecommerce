from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('productDetail/<int:id>/',views.product_detail_page,name="product_detail_page"),

    path('contact',views.contact_me_page,name="contact_me_page"),
    path('checkout/',views.checkOut_page,name="checkOut_page"),
]
