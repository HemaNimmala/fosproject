from django.shortcuts import render,redirect
from empmodule.models import Jobdetails
from .forms import ReviewForm
from .models import TouristReview

from requests import request


# Create your views here.
def viewfood(request):
    return render(request,'customermodule/viewfood.html')


def viewfood1(request):
    viewfood1=Jobdetails.objects.all()
    return render(request,'customermodule/viewfood.html',{'job_details_list':viewfood1})
def southveg(request):
    return render(request,'customermodule/southveg.html')
def deserts(request):
    return render(request,'customermodule/deserts.html')
def feedback(request):
    return render(request,'empmodule/feedback.html')
def aboutus(request):
    return render(request,'navbar/aboutus.html')
def review_list(request):
    if request.method == 'GET':
        reviews = TouristReview.objects.all()
        return render(request,'reviewpage.html',{'reviews':reviews})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review=form.save(commit=False)
            review.user=request.user
            review.save()
            return redirect('review_list')
        else:
            form = ReviewForm()
        return render(request,'reviewpage.html',{'form':form})


def addtocart(request):
    return render(request,'customermodule/Add_to_cart.html')
def ordernow(request):
    return render(request,'customermodule/order_now.html')

def profile1(request):
    return render(request,'customermodule/profile.html')

def payment(request):
    return render(request,'customermodule/paymenty.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def profile(request):
    user = request.user
    profile = UserProfile.objects.get_or_create(user=user)[0]
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        profile.bio = request.POST.get('bio')
        profile.save()
        return redirect('profile')

    return render(request, 'profile.html', {'user': user, 'profile': profile})

def cart(request):
    return render(request,'cart.html')

def paynow(request):
    return render(request,'customermodule/paynow.html')
from django.shortcuts import render, redirect
from .models import Product, CartItem

def cart_view(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    # Logic to add the product to the cart or update quantity if already in cart
    return redirect('cart_view')

# Other views for updating cart items, applying discounts, and removing items
