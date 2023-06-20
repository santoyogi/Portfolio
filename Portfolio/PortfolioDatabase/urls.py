from . import views
from django.urls import path

app_name = 'Portfolio'
urlpatterns = [
    path('', views.index, name="index"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('home/', views.home, name="home"),
    path('hobbies/<int:hobby_id>', views.detail, name="detail"),
    path('portfolio/<int:portfolio_id>', views.portfolio_detail, name="portfolio_detail"),
]