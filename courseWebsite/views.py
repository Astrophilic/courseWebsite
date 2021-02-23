from django.shortcuts import render


def home(request):
    return render(request, 'courseWebsite/home.html')


def cart(request):
    return render(request, 'courseWebsite/cart.html')


def checkout(request):
    return render(request, 'courseWebsite/checkout.html')
