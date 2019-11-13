from django.urls import path
from app1.views import home_view

urlpatterns=[
    path('',home_view),
]