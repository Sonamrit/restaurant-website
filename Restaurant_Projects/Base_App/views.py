from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request,'home.html')

def AboutView(request):
    pass

def MenuView(request):
    pass

def BookTableView(request):
    pass
