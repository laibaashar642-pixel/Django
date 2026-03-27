'''from django.shortcuts import render
from django.http import HttpResponse
def index(request):
   context={
       "variables":"this is sent",
    }
    return render(request,'index.html',context)'''
      context={
     "var1":"harry is great",
     "var2":"Laiba is great",
  }
  return render(request,'index.html',context)
    #return HttpResponse("Hello,World!")
def about(request):
    return HttpResponse("This is the about page!")
def services(request):
    return HttpResponse("This is my service page!")'''

# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from home.models import Contact

def index(request):
    context={
        "var1":"laiba is great",
        "var2":"harry is great",
    }
    messages.success(request,"This is a test message.")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        print("Name:", name)
        print("Phone:", phone)
        print("Email:", email)
        print("Description:", desc)

        # Save to database
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        # Success message
        messages.success(request, "Your message has been sent!")

        # Render template with context
        return render(request, 'contact.html', {
            'name': name,
            'description': desc,
            'email': email,
            'phone': phone,
        })

    # For GET request
    return render(request, 'contact.html')
