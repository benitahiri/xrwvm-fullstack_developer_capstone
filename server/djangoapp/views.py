# Uncomment the required imports before adding the code

 from django.shortcuts import render
 from django.http import HttpResponseRedirect, HttpResponse
 from django.contrib.auth.models import User
 from django.shortcuts import get_object_or_404, render, redirect
 from django.contrib.auth import logout
 from django.contrib import messages
 from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

@csrf_exempt
def logout_request(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({"status": "Logged out"})
    return JsonResponse({"error": "Invalid request method"}, status=400)


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        email = data.get('email', '')  # Optional field
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        
        return JsonResponse({"userName": username, "status": "Registered"})
    
    return JsonResponse({"error": "Invalid request method"}, status=400)


# # Update the `get_dealerships` view to render the index page with
def get_dealerships(request):
    # Assuming you have a `Dealership` model
    dealerships = Dealership.objects.all()
    return render(request, 'dealerships.html', {'dealerships': dealerships})


# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    # Assuming you have a `Review` model related to `Dealer`
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    reviews = Review.objects.filter(dealer=dealer)
    return render(request, 'dealer_reviews.html', {'dealer': dealer, 'reviews': reviews})


# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    # Assuming you have a `Dealer` model
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return render(request, 'dealer_details.html', {'dealer': dealer})


# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dealer_id = data['dealer_id']
        review_text = data['review_text']
        rating = data['rating']
        
        dealer = get_object_or_404(Dealer, pk=dealer_id)
        Review.objects.create(dealer=dealer, text=review_text, rating=rating)
        
        return JsonResponse({"status": "Review added"})
    
    return JsonResponse({"error": "Invalid request method"}, status=400)

