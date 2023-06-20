from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobbies
from .models import Portfolio
from django.template import loader


# Create your views here.
def index(request):
    context = {}
    return render(request, 'PortfolioDatabase/index.html', context)

def home(request):
    context = {}
    return render(request, 'PortfolioDatabase/home.html', context)

def hobbies(request):
    hobby_list = Hobbies.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'PortfolioDatabase/index.html', context)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'PortfolioDatabase/portfolio.html', context)


def contact(request):
    context = {}
    return render(request, 'PortfolioDatabase/contact.html', context)


def detail(request, hobby_id):
    hobby = Hobbies.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'PortfolioDatabase/detail.html', context)

def portfolio_detail(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'PortfolioDatabase/portfolio_detail.html', context)
