import imp
from .models import Listing
from django.forms import ModelForm


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'name',
            'description',
            'brand',
            'milage',
            'price',
            'image'
        ]
        