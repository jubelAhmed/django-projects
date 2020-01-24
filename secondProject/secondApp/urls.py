from django.urls import path
from secondApp import views 

urlpatterns = [
    path("",views.index , name = 'index'),
]