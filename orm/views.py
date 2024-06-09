from django.shortcuts import render
from .models import Client
from django.contrib.auth.decorators import login_required
from . import forms



# Create your views here.
def client_list(request):
    clients = Client.objects.all().order_by('-name')
    return render(request, 'klienci/client_list.html', {"clients": clients})

def client_page(request, slug):
    one_client = Client.objects.get(slug=slug)
    return render(request, 'klienci/client_page.html', {"client": one_client})

@login_required(login_url='/users_app/login')
def client_new(request):
    form = forms.CreateClient()
    return render(request, 'klienci/client_new.html', {"form": form})