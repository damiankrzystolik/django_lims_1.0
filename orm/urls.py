from django.urls import path
from . import views

app_name = 'orm'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('new-client', views.client_new, name='new-client'),
    path('client/<int:id>/<slug:slug>/', views.client_page, name='client_page'),
    path('client/<int:id>/<slug:slug>/edit/', views.edit_client, name='edit_client'),
    path('client/<int:id>/<slug:slug>/delete', views.delete_client, name='delete_client'),
    path('search/', views.search_client, name='search_client'),
]
