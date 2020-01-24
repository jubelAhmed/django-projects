from django.shortcuts import render
from secondApp.models import AccessRecord,WebPage,Topic

# Create your views here.

def index(request): 
    
    web_pages = AccessRecord.objects.order_by('date')
    
    web_dict = {'access_records':web_pages}
    
    return render(request,"secondApp/index.html",context=web_dict)




