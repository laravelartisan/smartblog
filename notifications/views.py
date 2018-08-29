from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views import View

# Create your views here.


class NewNotification (View):
    def get(self, request):
        return HttpResponse('welcome to notification view')