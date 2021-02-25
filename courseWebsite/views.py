from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'courseWebsite/home.html')


def cart(request):
    return render(request, 'courseWebsite/cart.html')


def checkout(request):
    return render(request, 'courseWebsite/checkout.html')


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'courseWebsite/register.html', context)
