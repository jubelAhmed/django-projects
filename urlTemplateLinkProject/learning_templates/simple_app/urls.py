from django.urls import path , include
from simple_app import views

# TEMPLATE TAGGING

app_name = 'simple_app'

urlpatterns = [
    path('base/',views.base,name='base'),
    path('other/',views.other,name='other'),
    path('relative/',views.base,name='relative'),
] 