from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for login
    path('login', views.login_user, name='login'),
    # other paths (like for reviews, etc.)
]