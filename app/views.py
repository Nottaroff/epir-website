from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def products(request):
    return render(request,'products.html')

def valores(request):
    return render(request,'valores.html')

def exosqueletos(request):
    return render(request,'exosqueletos.html')

def cascosinteligentes(request):
    return render(request,'cascosinteligentes.html')





