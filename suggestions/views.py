from django.shortcuts import render, redirect
from .models import Suggestion
from . import views


def index(request):
    return render(request, 'index.html')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        age = request.POST.get('age')
        gender = request.POST.get('gender', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        suggestion = request.POST.get('suggestion')
        notification = request.POST.getlist('notification')

        Suggestion.objects.create(
            name=name,
            age=age,
            gender=gender,
            email=email,
            phone=phone,
            suggestion=suggestion,
            notification=", ".join(notification)
        )

        return redirect('index')

    return render(request, 'index.html')
