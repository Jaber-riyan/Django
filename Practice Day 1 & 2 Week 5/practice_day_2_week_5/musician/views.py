from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
# def addmusician(request):
#     if request.method == 'POST':
#         form = forms.MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add_musician')
#     else:
#         form = forms.MusicianForm()
#         return render(request,'add_musician.html',{'form':form})

@method_decorator(login_required, name='dispatch')
class addmusician1(CreateView):
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    def get_success_url(self):
        messages.success(self.request,'Add Musician Successfully')
        return reverse_lazy('homepage')
    


    
