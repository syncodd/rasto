
from django.contrib import admin
from django.urls import path, include
from api.views import ZodiacView

urlpatterns = [
    path('zodiac/', ZodiacView.as_view())
]
