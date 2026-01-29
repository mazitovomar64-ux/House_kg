from rest_framework import serializers
from .models import (UserProfile, Region, City, District,
                     Property, PropertyImage, Review)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



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
        fields = ['username','comment']



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



