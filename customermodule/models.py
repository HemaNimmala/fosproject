from django.db import models
from django.shortcuts import render
# Create your models here.
def viewfood(request):
    return render(request,'customermodule/viewfood.html')

class TouristReview(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    image = models.FileField(upload_to='static/media/review_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


#
# class cart():
#     def __init__(self, request, ):
#         self.session=request.session
#         cart=self.session.get('session_key')
#         if 'session_key' not in request.session:
#             cart=self.session['session_key']={}
#         self.cart=cart


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
