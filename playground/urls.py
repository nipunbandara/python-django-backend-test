#map urls and views
from django.urls import path
from . import views

#urlConfigurations
urlpatterns = [
    path('hello/', views.say_hello),
]