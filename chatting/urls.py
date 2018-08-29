from django.urls import path
from chatting.views import *

urlpatterns = [
    path('send/', NewMessage.as_view(), name='send_meassage'),
]
