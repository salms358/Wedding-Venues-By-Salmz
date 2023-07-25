from django.shortcuts import render
from .models import Bookings, UserProfile


# Create your views here.
def create_profile(request):
    if request.method == "POST":
        

