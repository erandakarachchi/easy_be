from easy_res_api.models import Food,Restaurant,Orders,Customers
from rest_framework import viewsets,permissions
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .serializers import FoodSerializer,RestaurantSerializer,OrderSerializer,CustomerSerializer
from rest_framework.renderers import JSONRenderer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FoodSerializer
    
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes =[
        permissions.AllowAny
    ]
    serializer_class = RestaurantSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    #queryset = Orders.objects.all()
    queryset = Orders.objects.filter(total__gt=10) #__gt => grater than,
    permission=[
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer
    

class CustomerViewSet(viewsets.ModelViewSet):
    # queryset = Customers.objects.all()
    queryset = Customers.objects.select_related().all()
    permission=[
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer
    
    @action(detail=False,methods=['get'])
    def get_customer_names(self,request,pk=None):
        customer_query_set = Customers.objects.filter(id__gte = 1)
        permission=[
        permissions.AllowAny
            ]
        serializer_class = CustomerSerializer
        data =list(Customers.objects.filter(id__gte = 1))
        return JsonResponse(data, safe=False)
        
        
def customer_list(request):
    if request.method == 'GET':
        data = Customers.objects.filter(id=1)
        serializer = CustomerSerializer(data,many=True)
        headerInfo = {'Accept': 'application/json' }
        res = JsonResponse(data=serializer.data,safe=False)
        return res