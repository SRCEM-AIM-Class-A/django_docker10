#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is home page from index")


def about(request):
    return render(request, 'about.html') 
    # return HttpResponse("This is about page")

# def contact(request):
#     return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def home(request):
    return render(request, 'home.html')