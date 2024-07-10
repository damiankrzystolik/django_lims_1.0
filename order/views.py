from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.



def zlecenie(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Zamień 'success_url' na odpowiednią nazwę ścieżki
    else:
        form = OrderForm()

    return render(request, 'order/zlecenie.html', {'form': form})