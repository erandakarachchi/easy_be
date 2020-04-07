from django.urls import path
from rest_framework import routers
from .api import FoodViewSet,RestaurantViewSet,CustomerViewSet,OrderViewSet,customer_list
from  rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('api/foods',FoodViewSet,'foods')
router.register('api/restraurants',RestaurantViewSet,'restaurants')
router.register('api/customers',CustomerViewSet,'customers')
router.register('api/orders',OrderViewSet,'test_orders')

# urlpatterns =(
#     router.urls,
    
#     ) 
urlpatterns = [
    path('customer_list/', customer_list, name=''),
]

urlpatterns = format_suffix_patterns(urlpatterns)