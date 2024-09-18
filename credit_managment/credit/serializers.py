from rest_framework.serializers import ModelSerializer
from credit.models import CreditModel

class CreditSerializer(ModelSerializer):
	class Meta:
		model=CreditModel
		fields='__all__'