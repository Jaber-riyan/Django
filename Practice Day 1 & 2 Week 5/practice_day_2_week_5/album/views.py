from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy



# Create your views here.
# @login_required
# def addalbum(request):
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST)
#         if form.is_valid():
#             messages.success(request,'Add Album successfully')
#             form.save()
#             return redirect('addalbum')
        
#     else:
#         form = forms.AlbumForm()
#         return render(request,'addalbum.html',{'form':form})
    

@method_decorator(login_required, name='dispatch')
class addalbum1(CreateView):
    form_class = forms.AlbumForm
    template_name = 'addalbum.html'
    def get_success_url(self):
        return reverse_lazy('addalbum')
    
    def form_valid(self, form):
        messages.success(self.request, 'Add Album successfully')
        return super().form_valid(form)



    
    
    
    
# @login_required  
# def edit(request, id):
#     album = models.AlbumModel.objects.get(pk=id)
#     form = forms.AlbumForm(instance=album)
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST, instance=album)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')
    
#     else:
#         form = forms.AlbumForm(instance=album)    
#         return render(request,'addalbum.html',{'form':form})
    
    

@method_decorator(login_required, name='dispatch')
class edit1(UpdateView):
    model = models.AlbumModel
    template_name = 'addalbum.html'
    form_class = forms.AlbumForm
    pk_url_kwarg = 'id'
    def get_success_url(self):
        messages.success(self.request,'Update Successfully')
        return reverse_lazy('homepage')
    
    
    
   



    
# @login_required    
# def delete(request,id):
#     delete = models.AlbumModel.objects.get(pk=id)
#     delete.delete()
#     return redirect('homepage')
            


@method_decorator(login_required, name='dispatch')
class delete1(DeleteView):
    model = models.AlbumModel
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')  
    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['id'])