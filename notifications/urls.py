from django.urls import path
from notifications.views import *

urlpatterns = [
    path('create/', NewNotification.as_view(), name='create_notification'),
]
