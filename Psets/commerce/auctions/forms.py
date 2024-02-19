from django import forms
from .models import Listing, Category

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['auctioneer', 'title', 'start_bid', 'image_url', 'description', 'category']
        widgets = {
            'category': forms.Select(choices=Category.objects.values_list('category', 'category')),
        }