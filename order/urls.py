from django.urls import path
from .views import zlecenie

app_name = 'zlecenie'

urlpatterns = [
    path('zlecenie', zlecenie, name='zlecenie'),
]