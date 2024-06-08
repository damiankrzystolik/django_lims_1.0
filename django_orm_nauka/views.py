# from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("Hello, Django! Index page.")
    return render(request, 'index.html')

def form(request):
    # return HttpResponse("Orm page. Page with forms to add client.")
    return render(request, 'orm.html')