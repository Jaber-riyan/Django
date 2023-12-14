from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from practice_day_2_week_5.froms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from album.models import AlbumModel
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator




# def home(request):
#     data = AlbumModel.objects.all()
#     return render(request,'data.html',{'data':data})

class home1(ListView):
    model = AlbumModel
    template_name = 'data.html'
    context_object_name = 'data'


# def registerform(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             messages.success(request,'Sign Up Successfully')
#             form.save()
#             return redirect('register')
#     else:
#         form = RegisterForm()
#     return render(request,'register.html',{'form':form})


class registerForm1(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('register')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Sign Up Successfully')
        return response




# def userlogin(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             userpass = form.cleaned_data['password']
#             user = authenticate(username=username, password=userpass)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,'Logged In Successfully')
#                 return redirect('homepage')
            
#     else:
#         form = AuthenticationForm()   
#         return render(request,'login.html',{'form':form})
    

class userlogin1(LoginView):
    template_name = 'login.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Logged In Successfully')
        return response
    def get_success_url(self):
        return reverse_lazy('homepage')





    
# @login_required  
# def userlogout(request):
#     logout(request)
#     return redirect('login')

@method_decorator(login_required, name='dispatch')
class userlogout1(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Logged Out Successfully')
        return reverse_lazy('login')
        