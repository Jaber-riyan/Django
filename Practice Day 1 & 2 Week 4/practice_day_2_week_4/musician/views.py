from django.shortcuts import render,redirect
from musician.forms import MusicianForm

# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = MusicianForm()
        return render(request,'add_musician.html',{'form':form})
