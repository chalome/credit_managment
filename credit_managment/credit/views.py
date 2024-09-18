from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from credit.models import CreditModel
from credit.forms import CreditForm
from django.urls import reverse_lazy
from credit.serializers import CreditSerializer
from rest_framework.viewsets import ModelViewSet

class HomeView(TemplateView):
	template_name='credit/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
        # Get the logged-in user
		user = self.request.user
        # Fetch credits for the user
		user_credits = CreditModel.objects.filter(customer=user)
        # Check if any credits are approved
		approved_credits = user_credits.filter(approved=True)
		context['approved_credits'] = approved_credits
		context['user_credits'] = user_credits
		return context

class CreditCreateView(LoginRequiredMixin,CreateView):
	model=CreditModel
	form_class=CreditForm
	template_name='credit/credit.html'
	success_url=reverse_lazy('credit_list')

	def form_valid(self, form):
		form.instance.customer = self.request.user
		return super().form_valid(form)

class CreditListView(LoginRequiredMixin,ListView):
	model=CreditModel
	template_name='credit/credit_list.html'
	paginate_by=5

class CreditDetailView(LoginRequiredMixin,DetailView):
	model=CreditModel
	context_object_name='credit'
	template_name='credit/credit_detail.html'

class CreditUpdateView(LoginRequiredMixin,UpdateView):
	model=CreditModel
	template_name='credit/credit_update.html'
	form_class=CreditForm
	success_url=reverse_lazy('credit_list')

	def get_object(self,queryset=None):
		return get_object_or_404(CreditModel,id=self.kwargs['credit_id'])

class CreditDeleteView(LoginRequiredMixin,DetailView):
	model=CreditModel
	template_name='credit/credit_delete.html'
	success_url=reverse_lazy('credit_list')

	def get_object(self,queryset=None):
		return get_object_or_404(CreditModel,id=self.kwargs['credit_id'])

class CreditViewSet(LoginRequiredMixin,ModelViewSet):
	queryset = CreditModel.objects.all()
	serializer_class = CreditSerializer

	# def list(self, request):
	# 	queryset = self.get_queryset()
	# 	serializer = self.get_serializer(queryset, many=True)
	# 	return Response(serializer.data)
