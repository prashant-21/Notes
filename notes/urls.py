"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

APP_NAME = 'notes'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]