from django import forms
from authentication.models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model=CustomUser
		fields=['username','email','gender','civility','province','birth_year','profile_photo']

class LoginForm(AuthenticationForm):
	username=forms.CharField(max_length=128,label='Username')
	password=forms.CharField(max_length=129,widget=forms.PasswordInput,label='Password')

class ChangePasswordForm(forms.Form):
	old_password=forms.CharField(widget=forms.PasswordInput,label='Old password')
	new_password=forms.CharField(widget=forms.PasswordInput,label='New password')
	Confirm_password=forms.CharField(widget=forms.PasswordInput,label='confirm password')