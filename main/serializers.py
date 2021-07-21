from rest_framework import serializers
from .models import Food
from .models import Paleo
from .models import Vegetarian
from .models import Vegan
from .models import Ketogenic
from .models import Mediterranean
from .models import news

class FoodSerializer(serializers.ModelSerializer):
	class Meta:
		model = Food
		fields ='__all__'

class PaleoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paleo
		fields ='__all__'

class VegetarianSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vegetarian
		fields ='__all__'

class VeganSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vegan
		fields ='__all__'

class KetogenicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ketogenic
		fields ='__all__'

class MediterraneanSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mediterranean
		fields ='__all__'

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = news
		fields ='__all__'