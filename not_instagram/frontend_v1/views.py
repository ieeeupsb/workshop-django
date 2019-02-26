from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template('frontend_v1/home.html')
    context = {
        'title': 'Homepage | !instagram',
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('frontend_v1/login.html')
    context = {
        'title': 'Login | !instagram',
    }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('frontend_v1/register.html')
    context = {
        'title': 'Register | !instagram',
    }
    return HttpResponse(template.render(context, request))
