from django.shortcuts import render
from . import forms
from . import forms2

# Create your views here.
def home(request):
    return render(request,'first_app/home.html')


def form(request):
    form = forms.FormExample()
    return render(request,'first_app/form.html',{'form':form})


def model(request):
    model = forms2.ModelOfFirst
    return render(request,'first_app/model.html',{'model':model})
