from django.urls import path
from . import views


urlpatterns = [
    # path('addalbum/',views.addalbum,name='addalbum'),
    path('addalbum/',views.addalbum1.as_view(),name='addalbum'),
    # path('edit/<int:id>/',views.edit,name='editalbum'),
    path('edit/<int:id>/',views.edit1.as_view(),name='editalbum'),
    # path('delete/<int:id>/',views.delete,name='deletealbum'),
    path('delete/<int:id>/',views.delete1.as_view(),name='deletealbum'),
]
