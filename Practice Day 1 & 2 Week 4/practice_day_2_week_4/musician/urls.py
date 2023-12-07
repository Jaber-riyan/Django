from django.urls import path
from . import views

urlpatterns = [
    path('addmusician/',views.add_musician,name='add_musician'),
]