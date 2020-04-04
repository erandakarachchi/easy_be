from easy_res_api.models import Food
from rest_framework import viewsets,permissions
from .serializers import FoodSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FoodSerializer