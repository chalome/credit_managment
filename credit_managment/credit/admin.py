from django.contrib import admin
from credit.models import CreditModel

class CreditAdmin(admin.ModelAdmin):
	list_display=('customer','amount','date_created','approved','payed')

admin.site.register(CreditModel,CreditAdmin)