from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404

# Create your views here.

class SignUp (View):
    def get(self, request):
        return HttpResponse('Welcome to signup view')
