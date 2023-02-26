from django.urls import path, include
from django.contrib import admin
from . import views
from study_tracker import views

from main.views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path(r'^tracker/$', include('study_tracker.urls'))
]