from django import forms
from credit.models import CreditModel


class CreditForm(forms.ModelForm):
	class Meta:
		model=CreditModel
		fields=['amount']

