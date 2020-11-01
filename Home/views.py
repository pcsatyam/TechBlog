from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse ("This is Home page")

def mobile(request):
    return render(request, 'mobile.html')

def laptop(request):
    return render(request, 'laptop.html')

def other(request):
    return render(request, 'other.html')

def older(request):
    return render(request, 'older.html')

def Home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name=name, email=email)
        contact.save()
        messages.success(request, 'You are succesfully subscribed')
    return render(request, 'contact.html')
