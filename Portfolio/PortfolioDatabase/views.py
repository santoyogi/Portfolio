from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobbies
from .models import Portfolio


# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def home(request):
    return HttpResponse("Welcome to my portfolio! "
                        "My name is Gissel. I am a student at Weber State "
                        "University, and I am studying to get my degree "
                        "in CS!")

def hobbies(request):
    hobby_list = Hobbies.objects.all()
    return HttpResponse(hobby_list)

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)


def contact(request):
    return HttpResponse("Email: gisselsantoyo@mail.weber.edu")
