from django.urls import path
from .views import UserContact

urlpatterns = [
    path('contact', UserContact, name='contact'),
]
