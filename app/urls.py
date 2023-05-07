from app import views
from django.urls import path, include

urlpatterns = [
    path('',views.home, name="home"),
    path('contact',views.contact, name="contact"),
    path('about',views.about, name="about"),
    path('products',views.products, name="products"),
    path('valores',views.valores, name="valores"),
    path('exosqueletos',views.exosqueletos, name="exosqueletos"),
    path('cascosinteligentes',views.cascosinteligentes, name="cascosinteligentes"),
]
