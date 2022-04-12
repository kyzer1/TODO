from django import views
from django.contrib import admin
from .models import Todo

admin.site.register(Todo)
