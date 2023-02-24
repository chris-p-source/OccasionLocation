from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1> hello world</h1>")
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	
	return render(request, "about.html", {})

def faq_view(request, *args, **kwargs):
	
	return render(request, "faq.html", {})

def login_view(request, *args, **kwargs):
	
	return render(request, "login.html", {})

def signup_view(request, *args, **kwargs):
	
	return render(request, "signup.html", {})




def addevent_view(request, *args, **kwargs):
	
	return render(request, "addevent.html", {})

def settings_view(request, *args, **kwargs):
	
	return render(request, "settings.html", {})

def results_view(request, *args, **kwargs):
	
	return render(request, "results.html", {})




	