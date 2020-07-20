from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Companies


# Create your views here.
@login_required
def dashboard(request):
    company_data = Companies.objects.all()

    context ={'company':company_data}
    return render(request, "software/dashboard.html", context)

