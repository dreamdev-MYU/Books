from django.shortcuts import render
from django.urls import reverse

def base_page(request):
    # Correct the redirect URL here
    return render(request, 'base.html')
