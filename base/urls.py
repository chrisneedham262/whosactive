from django.urls import path
from .views import home, about, contact, faqs, insight, jobs

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faqs/', faqs, name='faqs'),
    path('insight/', insight, name='insight'),
    path('jobs/', jobs, name='jobs'),
    
    
   
]

