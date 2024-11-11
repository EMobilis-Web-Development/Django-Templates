from django.shortcuts import render


def home(request):
  return render(request,'home.html')


def women(request):
    return render(request,'women.html')

def men(request):
    return render(request,'men.html')

def about(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contacts.html')