from django.shortcuts import render
from .models import Cliente

def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'home.html', {'clientes': clientes})
