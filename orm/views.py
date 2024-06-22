from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='/users_app/login')
def client_list(request):
    clients = Client.objects.all().order_by('name')
    return render(request, 'klienci/client_list.html', {"clients": clients})

def client_page(request, id, slug):
    one_client = Client.objects.get(id=id, slug=slug)
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

# @login_required(login_url='/users_app/login')
def edit_client(request, id, slug):
    # return HttpResponse("Hello, Django! Index page.")

    client = Client.objects.get(id=id, slug=slug)
    print('1')
    if request.method == 'POST':
        form = forms.ClientForm(request.POST, request.FILES, instance=client)
        print('2')
        if form.is_valid():
            form.save()
            return redirect('orm:client_list')
            print('3')
        else:
            form = forms.ClientForm(instance=client)
            print('4')
    else:
      form = forms.ClientForm(instance=client)
      print('5')
      return render(request, 'klienci/edit_client.html', {'form': form, 'client': client})
    return render(request, 'klienci/edit_client.html', {'form': form, 'client': client})

def delete_client(request, id, slug):
    client = Client.objects.get(id=id, slug=slug)
    if request.method == 'POST':
        client.delete()
        return redirect('orm:client_list')
    return redirect('orm:client_detail', id=id)