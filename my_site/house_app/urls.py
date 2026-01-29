from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, RegionListAPIView, RegionDetailAPIView, CityListAPIView,
                    CityDetailAPIView, DistrictListAPIView, DistrictDetailAPIView,
                    PropertyListAPIView, PropertyDetailAPIView, PropertyImageViewSet, ReviewViewSet,PropertyCreateAPIView,PropertyEditAPIView)

router = routers.DefaultRouter()


router.register('users', UserProfileViewSet),
router.register('property_images', PropertyImageViewSet),
router.register('reviews', ReviewViewSet),


urlpatterns = [
    path('', include(router.urls)),
    path('property/', PropertyListAPIView.as_view(), name='property_list'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property_detail'),
    path('property/create/', PropertyCreateAPIView.as_view(), name='property_detail'),
    path('property/<int:pk>/edit/', PropertyEditAPIView.as_view(), name='property_detail'),
    path('region/', RegionListAPIView.as_view(), name='region_list'),
    path('region/<int:pk>/', RegionDetailAPIView.as_view(), name='region_detail'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('district/', DistrictListAPIView.as_view(), name='district_list'),
    path('district/<int:pk>/', DistrictDetailAPIView.as_view(), name='district_detail'),
]