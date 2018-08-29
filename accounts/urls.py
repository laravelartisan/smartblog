from django.urls import path
from accounts.views import *


urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
]
