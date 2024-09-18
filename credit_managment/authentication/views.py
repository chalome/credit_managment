from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from authentication.models import CustomUser
from authentication.forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView
from authentication.forms import LoginForm
from django.views import View
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView
from authentication.forms import ChangePasswordForm

class UserCreationView(CreateView):
	model=CustomUser
	template_name='authentication/signup.html'
	success_url=reverse_lazy('credit_home')
	form_class=UserForm

	def form_valid(self,form):
		user=form.save()
		login(self.request, user)
		return redirect(settings.LOGIN_REDIRECT_URL)
	def form_invalid(self,form):
		message='Error'
		return render(self.request, self.template_name,context={'message':message,'form':form})

class CustomLoginView(LoginView):
	template_name='authentication/login.html'
	authentication_form=LoginForm

class CustomLogoutView(View):
	def get(self,request):
		logout(request)
		return redirect('login')

class userListView(ListView):
	model=CustomUser
	template_name='authentication/users_list.html'
	paginate_by = 3

class UserUpdateView(UpdateView):
	model=CustomUser
	form_class=UserForm
	template_name='authentication/users_update.html'
	context_object_name='users'
	success_url=reverse_lazy('user_list')

	def get_object(self,queryset=None):
		return get_object_or_404(CustomUser,id=self.kwargs['user_id'])

class UserDeleteView(DeleteView):
	model=CustomUser
	template_name='authentication/users_delete.html'
	success_url=reverse_lazy('user_list')

	def get_object(self,queryset=None):
		return get_object_or_404(CustomUser,id=self.kwargs['user_id'])

class ChangePasswordView(PasswordChangeView):
	form_class=ChangePasswordForm
	template_name='authentication/change_password.html'
	success_url=reverse_lazy('credit_home')