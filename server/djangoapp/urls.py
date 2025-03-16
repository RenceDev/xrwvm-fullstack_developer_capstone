from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for login
    path('login/', views.login_user, name='login'),
    # Path for adding a review
    path('add_review', views.add_review, name='add_review'),
    # Other paths for reviews, etc.
    path('get_cars', views.get_cars, name='getcars'),
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
]
