from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context={
       "variables":"this is sent",
    }
    return render(request,'index.html')
    #return HttpResponse("Hello,World!")
def about(request):
    return HttpResponse("This is the about page!")
def services(request):
    return HttpResponse("This is my service page!")

# Create your views here.
