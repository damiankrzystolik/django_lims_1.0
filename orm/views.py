from django.shortcuts import render
from .models import Client
from django.http import HttpResponse


# Create your views here.
def client_list(request):
    clients = Client.objects.all().order_by('name')
    return render(request, 'klienci/client_list.html', {"clients": clients})

def client_page(request, slug):
    one_client = Client.objects.all().order_by('name')
    # return render(request, 'klienci/client_list.html', {"orm": orm})
    return HttpResponse(slug)
