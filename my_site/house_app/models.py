from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator



class UserProfile(AbstractUser):
    phone_number = PhoneNumberField
    Role_Choices = (
    ('seller',  'seller'),
    ('buyer',  'buyer')
    )
    role = models.CharField(max_length=32)
    avatar = models.ImageField(upload_to='user_image')
    data_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.role}'


class Region(models.Model):
    region_name = models.CharField(max_length=32)

    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length=32)
    region = models.ForeignKey(Region ,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=32)

    def __str__(self):
        return self.district_name


class Property(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    PropertyType = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('studio', 'studio'),
    )
    property_type = models.CharField(max_length=32, choices=PropertyType)
    region = models.ForeignKey(Region , on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_photo')
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    area = models.IntegerField()
    price = models.PositiveSmallIntegerField()
    rooms = models.IntegerField()
    floor = models.IntegerField()
    total_floor = models.IntegerField()
    Condiction_Type =(
    ('под самоделку', 'под самоделку'),
    ('евроремонт', 'евроремонт'),
    ('хорошее', 'хорошее'),
    ('среднее', 'среднее'),
    ('не достроено', 'не достроено'),
)
    condition = models.CharField(max_length=32, choices=Condiction_Type)
    documents = models.BooleanField(default=False)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_average_rating(self):
        ratings = self.review_property.all()
        if ratings.exists():
            return round(sum([i.rating for i in ratings]) / ratings.count(), 2)
        return 0

    def get_count_people(self):
        return self.review_property.count()


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_photo')
    image = models.ImageField(upload_to='property_image')


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='review_property')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='buyer_review')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner_review')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField()
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment






