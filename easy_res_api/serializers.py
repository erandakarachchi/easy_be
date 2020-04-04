from rest_framework import serializers
from easy_res_api.models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'