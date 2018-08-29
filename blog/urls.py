from django.urls import path
from blog.views import *

urlpatterns = [
    path('posts/create/', PostCreation.as_view(), name='create_post'),
]
