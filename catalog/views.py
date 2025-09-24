from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def answer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f'Спасибо, {name}! Мы с вами свяжемся в ближайшее время.')
    return render(request, 'contacts.html')
