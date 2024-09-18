from django.db import models
from authentication.models import CustomUser

class CreditModel(models.Model):
	customer=models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name='CustomUser')
	amount=models.PositiveIntegerField(verbose_name='Amount')
	date_created = models.DateTimeField(auto_now_add=True)
	approved=models.BooleanField(default=False)
	payed=models.BooleanField(default=False)

	def __str__(self):
		return self.customer.username