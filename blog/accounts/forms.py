from django import forms
from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
		)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		
		if username and password:
			user = authenticate(username=username, password=password)	
			if not user:
				raise forms.ValidationError("The Username or Password is wrong, the user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("The Password is incorrect")
			if not user.is_active:
				raise forms.ValidationError("The User is no longer active")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
	email = forms.EmailField(label="Email address")
	email2 = forms.EmailField(label="Confirm Email")
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
	
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',
			'password2',
		 	]	


 	# def clean(self):
 	# 	email = self.cleaned_data.get("email")
		# email2 = self.cleaned_data.get("email2")
		# if email != email2:
		# 	raise forms.ValidationError("Email addess does not match.")

		# email_qs = User.objects.filter(email=email)
		# if email_qs.exists():
		# 	raise forms.ValidationError("This Email has already been registered")
		# password = self.cleaned_data.get("password")
		# password2 = self.cleaned_data.get("password2")
		# if password != password2:
		# 	raise forms.ValidationError("Passwords does not match.")

		# return super(UserRegistrationForm, self).clean(*args, **kwargs)
		


	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Email addess does not match.")

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This Email has already been registered")
		return email

	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Passwords does not match.")

		return password











