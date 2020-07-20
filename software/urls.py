from django.urls import path
from .views import dashboard

app_name='company'

urlpatterns = [
    path('', dashboard),
   
]

