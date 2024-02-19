from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):

    CATEGORIES = [
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Books', 'Books'),
        ('Home and Garden', 'Home and Garden'),
    ]


    category_name = models.CharField(max_length=255, choices=CATEGORIES)
    
    def __str__(self):
        return f"{self.category_name}"

class Listing(models.Model):
    auctioneer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="auctioneer")
    title = models.CharField(max_length=255)
    start_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    image_url = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")

    def __str__(self):
        return f"{self.title}"

    


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    bid_in_time = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing")

    def __str__(self):
        return f"{self.bid} {self.bid_in_time}"


class Comments(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment_date = models.DateTimeField
    

    def __str__(self):
        return f"{self.comment} {self.comment_date}"
    
class Watchlist(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField(Listing)

    def __str__(self):
        return f"{self.listings}"
    
class Winner(models.Model):
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE)
    winner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Winner of (self.listing.title)"
