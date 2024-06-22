from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = forms.CreateClient(request.POST, request.FILES)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.author = request.user
            new_client.save()
            return redirect('orm:client_list')
    else:
        form = forms.CreateClient()
    return render(request, 'klienci/client_new.html', {"form": form})