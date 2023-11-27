from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    d = {'author' : 'Jaber', 'age' : 2,'height' : "5'7",'birthday':datetime.datetime.now() , 'summation':20,'capfirst':'django','cutFilter':'january - february - march','list':['python','django','database'], 'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fees' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fees' : 10000
        },
        {
            'id' : 3,
            'name' : 'Database',
            'fees' : 8000
        }
        
    ]}
    return render(request,"first_app/home.html", d)