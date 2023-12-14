from django.urls import path
from . import views


urlpatterns = [
    # path('addmusician/',views.addmusician,name='addmusician'),
    path('addmusician/',views.addmusician1.as_view(),name='addmusician'),
]
