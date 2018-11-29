from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'aplicacion/index.php')

def contact(request):
	return render(request,'aplicacion/contact.php')

def about(request):
	return render(request,'aplicacion/about.php')

def users(request):
	return render(request,'aplicacion/users.php')


