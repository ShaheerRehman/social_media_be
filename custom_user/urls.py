from django.urls import path, include
from .views import CustomUserViewSet, CustomObtainAuthToken, ListBuildingView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', CustomUserViewSet)

urlpatterns = [
    path('token/', CustomObtainAuthToken.as_view()),
    path('buildings/', ListBuildingView.as_view(), name='building-list'),
    path('', include(router.urls)),
]
