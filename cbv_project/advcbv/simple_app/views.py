from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):  
    
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['welcome'] = 'Wlecome to Visit This website  '
        return context 
        

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'simple_app/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School
    
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('simple_app:list') 
    
    