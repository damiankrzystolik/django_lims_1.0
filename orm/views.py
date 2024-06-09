from django.shortcuts import render
from .models import Client



# Create your views here.
def client_list(request):
    clients = Client.objects.all().order_by('-name')
    return render(request, 'klienci/client_list.html', {"clients": clients})

def client_page(request, slug):
    one_client = Client.objects.get(slug=slug)
    return render(request, 'klienci/client_page.html', {"client": one_client})

