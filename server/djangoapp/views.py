# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel  # Added imports for CarMake and CarModel
from .populate import initiate  # Import the initiate function to populate data

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
    # Try to check if provided credentials can be authenticated
    user = authenticate(username=username, password=password)
    response_data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        response_data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(response_data)

# Create a `logout_request` view to handle sign out request
@csrf_exempt
def logout_request(request):
    logout(request)
    return JsonResponse({"status": "logged_out"})

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    return JsonResponse({"status": "User created", "user": {"username": user.username, "first_name": user.first_name, "last_name": user.last_name, "email": user.email}})

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    dealerships = Dealer.objects.all()  # Assuming you have a Dealer model
    dealership_list = []
    for dealership in dealerships:
        dealership_list.append({"name": dealership.name, "location": dealership.location, "id": dealership.id})
    return JsonResponse({"dealerships": dealership_list})

# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    reviews = Review.objects.filter(dealer_id=dealer_id)  # Assuming you have a Review model
    review_list = []
    for review in reviews:
        review_list.append({
            "username": review.user.username,
            "review": review.review_text,
            "rating": review.rating,
            "date": review.date,
        })
    return JsonResponse({"reviews": review_list})

# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)  # Assuming you have a Dealer model
    dealer_details = {
        "name": dealer.name,
        "location": dealer.location,
        "contact": dealer.contact_info,
        "website": dealer.website,
    }
    return JsonResponse({"dealer": dealer_details})

# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request):
    data = json.loads(request.body)
    dealer_id = data['dealerId']
    user = request.user
    review_text = data['reviewText']
    rating = data['rating']
    review = Review.objects.create(dealer_id=dealer_id, user=user, review_text=review_text, rating=rating)
    return JsonResponse({"status": "review_added", "review": {"username": user.username, "review": review_text, "rating": rating}})

# New `get_cars` method to retrieve car makes and models
def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if(count == 0):
        initiate()  # Populate data if no CarMake exists
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels": cars})
