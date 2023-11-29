from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'name':'Jaber Ahmed Riyan',
         'list':[1,2,3,4,5],'value':['j','a','b','e','r'],
         'date':datetime.datetime.now(), 'empty':"",
         'add' : 20 ,
         'capfirst' : 'riyan', 
         'cut':'Jaber - Ahmed',
         'dictsort' :[
        {'name' : 'jaber', 'age' : 18},
        {'name' : 'Riyan', 'age' : 40},
        {'name' : 'Joy', 'age' : 23},],
         'linenumber' : ['Jaber'], 
         'lower' : 'JABER', 
         'upper':'jaber',
         'title' : 'I AM jaber AHMED riyan', 
         'random' :['Jaber','Ahmed','Riyan'],}
    return render(request, 'first_app/index.html',context=d)
