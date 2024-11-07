from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, TaskViewSet,AdviceViewSet

router = DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'advice', AdviceViewSet)

urlpatterns = [
   
    path('', include(router.urls)),
]
