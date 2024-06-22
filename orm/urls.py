from django.urls import path
from . import views

app_name = 'orm'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('new-client', views.client_new, name='new-client'),
    path('<slug:slug>', views.client_page, name='client_page'),
]
