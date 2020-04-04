from rest_framework import routers
from .api import FoodViewSet


router = routers.DefaultRouter()
router.register('api/foods',FoodViewSet,'foods')

urlpatterns = router.urls