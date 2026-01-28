from rest_framework import serializers
from .models import (UserProfile, Region, City, District,
                     Property, PropertyImage, Review)



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name']


class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district_name']


class DistrictDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district_name']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class PropertyListSerializer(serializers.ModelSerializer):
    property_photo = PropertyImageSerializer(many=True, read_only=True)
    city = CityListSerializer()
    class Meta:
        model = Property
        fields = ['id', 'title', 'property_photo', 'city', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'



class PropertyDetailSerializer(serializers.ModelSerializer):
    property_photo = PropertyImageSerializer(many=True, read_only=True)
    city = CityListSerializer()
    average_rating = serializers.SerializerMethodField()
    seller = UserProfileNameSerializers()
    review_property = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = ['id', 'property_photo', 'city','title', 'property_type', 'price',
                  'region', 'district', 'address', 'area', 'rooms', 'floor',
                  'total_floor', 'condition', 'documents', 'description', 'seller', 'average_rating', 'review_property']

    def get_average_rating(self, obj):
        return obj.get_average_rating()



