from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()


class GuestForm(forms.Form):
	email =forms.EmailField(
						widget=forms.EmailInput(
								attrs={
								"class":"form-control",
								"placeholder":"Enter Email"}))


class LoginForm(forms.Form):
	username=forms.CharField(
					widget=forms.TextInput(
									attrs={
									"class":"form-control",
									"placeholder":"Enter UserName",}))
	password=forms.CharField(
					widget=forms.PasswordInput(
									attrs={
									"class":"form-control",
									"placeholder":"Enter Password",}))
	

class RegisterForm(forms.Form):
	username=forms.CharField(
					widget=forms.TextInput(
									attrs={
									"class":"form-control",
									"placeholder":"Enter UserName"}))
	email=forms.EmailField(
					widget=forms.EmailInput(
									attrs={
									"class":"form-control",
									"placeholder":"Enter Email"}))
	password=forms.CharField(
					widget=forms.PasswordInput(
									attrs={
									"class":"form-control",
									"placeholder":"Enter Password"}))
	confirm_password=forms.CharField(
					label="Confirm Password",
					widget=forms.PasswordInput(
									attrs={
									"class":"form-control",
									"placeholder":"Enter Password"}))
	def clean_username(self):
		username=self.cleaned_data.get("username")
		qs=User.objects.filter(username=username)   # dont make spelling mistakes
		if qs.exists():
			raise forms.ValidationError("Username Exists")
		return username
	def clean_email(self):
		email=self.cleaned_data.get("email")
		qs=User.objects.filter(email=email)   # dont make spelling mistakes
		if qs.exists():
			raise forms.ValidationError("Email Exists")
		return email

	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get("password")
		confirm_password=self.cleaned_data.get("confirm_password")
		if  password != confirm_password:
			raise forms.ValidationError("Password not matched")
		return data