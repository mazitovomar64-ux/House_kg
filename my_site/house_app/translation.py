from .models import Region,City,Property
from modeltranslation.translator import TranslationOptions,register

@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('region_name', )

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name', )


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title','description','address' )
