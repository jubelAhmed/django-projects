from django.shortcuts import render

# Create your views here.

def index(request):
    dict = {'text':'This is my country','number':100}
    return render(request,'simpleApp/index.html',dict)
    
def base(request):
    return render(request,'simpleApp/base.html')
    
def other(request):
    return render(request,'simpleApp/other.html')
    
def relative(request):
    return render(request,'simpleApp/relative_url.html')