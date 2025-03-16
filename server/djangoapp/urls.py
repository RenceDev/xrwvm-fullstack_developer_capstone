from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for login
    path('login/', views.login_user, name='login'),  # Ensure this matches the path in djangoproj/urls.py
    # other paths for reviews, etc.
    path('get_cars', views.get_cars, name='getcars'),  # Add this line
]
