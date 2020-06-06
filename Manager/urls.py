"""
#MANAGER
"""

from django.contrib import admin
from django.urls import path
from . import views


app_name = 'Manager'

urlpatterns = [
	path('', views.home, name='home'),
	
]
