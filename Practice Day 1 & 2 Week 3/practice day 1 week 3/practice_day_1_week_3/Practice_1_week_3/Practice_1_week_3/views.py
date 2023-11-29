from django.http import HttpResponse
from django.shortcuts import render

def home_main(request):
    return render(request,'home_main.html')