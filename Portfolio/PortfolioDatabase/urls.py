from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('home/', views.home, name="home"),
]