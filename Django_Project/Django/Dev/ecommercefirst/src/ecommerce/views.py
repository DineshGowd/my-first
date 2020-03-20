from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import ContactForm
from django.contrib.auth.models import User

def home_page(request):
	return HttpResponse("<h1>Hello, Django!</h1>")

def home_page_new(request):
	if request.session.get('_auth_user_id') == None:
		user="Guest"
	else:
		uid=request.session.get('_auth_user_id')
		user = User.objects.get(pk=uid)
		print(user)
	context={
	"title":"Home Page",
	"logged_user":user,
	"sec_para_1":"I am paragraph of home page",
	}
	if request.user.is_authenticated:
		context["premium_content"]="Welcome Premium customer"
	
	return render(request,"homepage.html",context)

def about_page(request):
	context={
	"title":"About Page",
	"heading_1":"I am About Page",
	"sec_para_1":"I am paragraph of about page",
	}
	return render(request,"homepage.html",context)

def contact_page(request):
	contact_form=ContactForm(request.POST or None)

	context={ 
		#purely all variables can be changed to any name 
			"title":"Contact Page",
			"sec_para_1":"I am paragraph of contact page",
			"form":contact_form,
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	if request.method=="POST":
		print(request.POST)
		print(request.POST.get("fullname"))
		print(request.POST.get("email"))
		print(request.POST.get("content"))

	return render(request,"contact/view.html",context)

def home_page_old(request):
	html_="""
	<!doctype html>
	<html lang="en">
	  <head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

	    <title>Hello, Old Django!</title>
	  </head>
	  <body>
	    <h1>Hello, Old Django!</h1>

	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
	  </body>
	</html>
	"""
	return HttpResponse(html_)