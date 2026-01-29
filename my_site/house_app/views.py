from rest_framework import viewsets, generics,permissions
from .models import (UserProfile, Region, City, District,
                     Property, PropertyImage, Review)
from .serializers import (UserProfileSerializer, RegionListSerializer, RegionDetailSerializer ,CityListSerializer,
                          CityDetailSerializer, DistrictListSerializer, DistrictDetailSerializer,
                          PropertyListSerializer, PropertyDetailSerializer, PropertySerializers,
                          PropertyImageSerializer, ReviewSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PropertyFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import PropertyPagination
from .permission import CheckRole,CheckOwner




class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [CheckRole]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer


class RegionDetailAPIView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer


class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer



class DistrictListAPIView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictListSerializer


class DistrictDetailAPIView(generics.RetrieveAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictDetailSerializer



class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ['title']
    ordering_fields = ['price']
    pagination_class = PropertyPagination
    permissions_class = [CheckOwner]



class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer


class PropertyCreateAPIView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class PropertyEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

