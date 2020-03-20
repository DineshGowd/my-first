from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils.http import is_safe_url


from .models import GuestEmail
from .forms import LoginForm,RegisterForm,GuestForm

def guest_register_view(request):
	form = GuestForm(request.POST or None)
	context={ 
			"title":"Guest Page",
			"form":form,
	}
	print("user logged in")
	next_=request.GET.get('next')
	next_post=request.POST.get('next')
	redirect_path = next_ or next_post or None

	if form.is_valid():
		print(form.cleaned_data)
		email    = form.cleaned_data.get("email")
		new_guest_email = GuestEmail.objects.create(email=email)
		request.session['guest_email_id']=new_guest_email.id

		if is_safe_url(redirect_path,request.get_host()):
			return redirect(redirect_path)
		else:
			return redirect("/register")
	return redirect("/register")



def login_page(request):
	form = LoginForm(request.POST or None)
	context={ 
			#purely all variables can be changed to any name 
			"title":"Login Page",
			"form":form,
	}
	print("user logged in")
	#print(request.user.is_authenticated)

	next_=request.GET.get('next')
	next_post=request.POST.get('next')
	redirect_path = next_ or next_post or None

	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		user = authenticate(request, username=username, password=password)
		print(user)
		#print(request.user.is_authenticated)
		if user is not None:
			try:
				del request.session['guest_email_id']
			except:
				pass
			login(request, user)
			if is_safe_url(redirect_path,request.get_host()):
				return redirect(redirect_path)
			else:
				return redirect("/home")
        	# Redirect to a success page.
			#context['form']=LoginForm()
			#print("hai buddy")
			# return redirect("/home")
		else:
			print("Error")

	return render(request,"accounts/login.html",context)


User=get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)

	context={ 
		#purely all variables can be changed to any name 
			"form":form,
			"title":"Register Page",
	}

	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user=User.objects.create_user(username,email,password)
		print(new_user)

	return render(request,"accounts/register.html",context)
