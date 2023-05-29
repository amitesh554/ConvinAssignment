from django.contrib import admin
from django.urls import path, include, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GoogleCalendarInitView, name=GoogleCalendarInitView),
]
